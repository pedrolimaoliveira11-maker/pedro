import sqlite3
from datetime import datetime

# --- CONFIGURAÇÃO DO BANCO ---

def conectar():
    """Conecta ao banco e ativa o suporte a Foreign Keys."""
    conn = sqlite3.connect('database.db')
    conn.execute("PRAGMA foreign_keys = ON")
    return conn

def inicializar_banco():
    """Cria tabelas e usuário inicial se não existirem."""
    with conectar() as conn:
        cursor = conn.cursor()
        # Usuários
        cursor.execute('CREATE TABLE IF NOT EXISTS usuarios (id INTEGER PRIMARY KEY AUTOINCREMENT, usuario TEXT UNIQUE, senha TEXT)')
        cursor.execute('INSERT OR IGNORE INTO usuarios (usuario, senha) VALUES ("admin", "123")')
        
        # Clientes
        cursor.execute('CREATE TABLE IF NOT EXISTS clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT NOT NULL, email TEXT)')
        
        # Produtos
        cursor.execute('CREATE TABLE IF NOT EXISTS produtos (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT NOT NULL, preco REAL, estoque INTEGER)')
        
        # Vendas
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS vendas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                cliente_id INTEGER NOT NULL,
                produto_id INTEGER NOT NULL,
                quantidade INTEGER NOT NULL,
                data TEXT NOT NULL,
                total REAL NOT NULL,
                FOREIGN KEY (cliente_id) REFERENCES clientes (id),
                FOREIGN KEY (produto_id) REFERENCES produtos (id)
            )
        ''')

# --- LOGICA DE VENDAS E RELATÓRIO ---

def registrar_venda():
    listar_clientes()
    listar_produtos()
    try:
        c_id = int(input("\nID do Cliente: "))
        p_id = int(input("ID do Produto: "))
        qtd = int(input("Quantidade: "))

        with conectar() as conn:
            cursor = conn.cursor()
            # Valida produto e estoque
            cursor.execute('SELECT nome, preco, estoque FROM produtos WHERE id = ?', (p_id,))
            prod = cursor.fetchone()
            
            if not prod:
                print("❌ Produto não encontrado!")
                return
            
            nome, preco, estoque = prod
            if estoque < qtd:
                print(f"❌ Estoque insuficiente! (Disponível: {estoque})")
                return

            # Processa a venda e baixa estoque em uma única transação
            total = preco * qtd
            data = datetime.now().strftime('%d/%m/%Y %H:%M')
            cursor.execute('INSERT INTO vendas (cliente_id, produto_id, quantidade, data, total) VALUES (?,?,?,?,?)', 
                           (c_id, p_id, qtd, data, total))
            cursor.execute('UPDATE produtos SET estoque = estoque - ? WHERE id = ?', (qtd, p_id))
            print(f"✅ Venda de {nome} realizada! Total: R$ {total:.2f}")

    except ValueError:
        print("❌ Digite números inteiros válidos para os IDs e Quantidade!")
    except sqlite3.IntegrityError:
        print("❌ Erro: ID de cliente ou produto inexistente!")

def ver_vendas():
    """Relatório corrigido com JOIN."""
    print("\n--- RELATÓRIO DE VENDAS ---")
    try:
        with conectar() as conn:
            cursor = conn.cursor()
            query = '''
                SELECT v.id, c.nome, p.nome, v.quantidade, v.total, v.data
                FROM vendas v
                JOIN clientes c ON v.cliente_id = c.id
                JOIN produtos p ON v.produto_id = p.id
                ORDER BY v.id DESC
            '''
            cursor.execute(query)
            vendas = cursor.fetchall()
            
            if not vendas:
                print("Nenhuma venda registrada.")
                return

            for v in vendas:
                total_formatado = float(v[4]) if v[4] else 0.0
                print(f"Venda #{v[0]} | Cliente: {v[1]} | Produto: {v[2]} | Qtd: {v[3]} | Total: R$ {total_formatado:.2f} | Data: {v[5]}")
    except sqlite3.OperationalError as e:
         print(f"❌ Erro no banco de dados: {e}")
         print("⚠️ Dica: Delete o arquivo 'database.db' antigo e rode novamente.")

# --- AUXILIARES E INTERFACE ---

def listar_clientes():
    with conectar() as conn:
        res = conn.execute('SELECT id, nome FROM clientes').fetchall()
        print("\nCLIENTES:", res)

def listar_produtos():
    with conectar() as conn:
        res = conn.execute('SELECT id, nome, estoque FROM produtos').fetchall()
        print("PRODUTOS:", res)

def login():
    print("\n" + "="*30)
    print("       TELA DE LOGIN")
    print("="*30)
    u = input("Usuário: ")
    s = input("Senha: ")
    with conectar() as conn:
        return conn.execute('SELECT * FROM usuarios WHERE usuario=? AND senha=?', (u, s)).fetchone()

def menu():
    inicializar_banco()
    
    if not login():
        print("\n🚫 Acesso negado. Usuário ou senha incorretos.")
        return

    print("\n✅ Acesso liberado!")
    
    while True:
        print("\n" + "="*30)
        print("1-Novo Cliente | 2-Novo Produto | 3-Venda | 4-Relatório | 0-Sair")
        op = input("Escolha: ")
        
        if op == "1":
            nome = input("Nome: ")
            email = input("Email (opcional): ")
            with conectar() as conn: 
                conn.execute('INSERT INTO clientes (nome, email) VALUES (?, ?)', (nome, email))
            print("✅ Cliente cadastrado!")
                
        elif op == "2":
            try:
                nome = input("Nome: ")
                preco = float(input("Preço: R$ ").replace(',', '.'))
                estoque = int(input("Estoque: "))
                with conectar() as conn: 
                    conn.execute('INSERT INTO produtos (nome, preco, estoque) VALUES (?,?,?)', (nome, preco, estoque))
                print("✅ Produto cadastrado!")
            except ValueError:
                print("❌ Erro: Digite números válidos para preço e estoque.")
                
        elif op == "3": 
            registrar_venda()
            
        elif op == "4": 
            ver_vendas()
            
        elif op == "0": 
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()