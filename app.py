import sqlite3
from datetime import datetime

def conectar():
    return sqlite3.connect('database.db')

def inicializar_banco():
    conn = conectar()
    cursor = conn.cursor()
    
    # Tabela de Clientes
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT
        )
    ''')
    
    # Tabela de Produtos
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            preco REAL NOT NULL,
            estoque INTEGER NOT NULL
        )
    ''')
    
    # Tabela de Vendas
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
    
    conn.commit()
    conn.close()

# --- Funções de Cadastro ---

def cadastrar_cliente(nome, email):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO clientes (nome, email) VALUES (?, ?)', (nome, email))
    conn.commit()
    conn.close()
    print(f"Cliente '{nome}' cadastrado!")

def cadastrar_produto(nome, preco, estoque):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO produtos (nome, preco, estoque) VALUES (?, ?, ?)', (nome, preco, estoque))
    conn.commit()
    conn.close()
    print(f"Produto '{nome}' cadastrado!")

def registrar_venda(cliente_id, produto_id, quantidade):
    conn = conectar()
    cursor = conn.cursor()
    
    # Busca preço e estoque do produto
    cursor.execute('SELECT nome, preco, estoque FROM produtos WHERE id = ?', (produto_id,))
    produto = cursor.fetchone()
    
    if produto and produto[2] >= quantidade:
        nome_prod, preco, estoque_atual = produto
        total = preco * quantidade
        data_venda = datetime.now().strftime('%d/%m/%Y %H:%M')
        
        # 1. Registra a venda
        cursor.execute('''
            INSERT INTO vendas (cliente_id, produto_id, quantidade, data, total)
            VALUES (?, ?, ?, ?, ?)
        ''', (cliente_id, produto_id, quantidade, data_venda, total))
        
        # 2. Baixa no estoque
        cursor.execute('UPDATE produtos SET estoque = ? WHERE id = ?', (estoque_atual - quantidade, produto_id))
        
        conn.commit()
        print(f"Venda registrada: {quantidade}x {nome_prod} | Total: R$ {total:.2f}")
    else:
        print("Erro: Estoque insuficiente ou produto inexistente.")
    
    conn.close()

# --- Relatório ---

def ver_vendas():
    conn = conectar()
    cursor = conn.cursor()
    # Join para mostrar nomes em vez de apenas IDs
    query = '''
        SELECT v.id, c.nome, p.nome, v.quantidade, v.total, v.data
        FROM vendas v
        JOIN clientes c ON v.cliente_id = c.id
        JOIN produtos p ON v.produto_id = p.id
    '''
    cursor.execute(query)
    print("\n--- LISTA DE VENDAS ---")
    for linha in cursor.fetchall():
        print(f"ID: {linha[0]} | Cliente: {linha[1]} | Prod: {linha[2]} | Qtd: {linha[3]} | Total: R$ {linha[4]:.2f} | Data: {linha[5]}")
    conn.close()

# --- Execução ---

if __name__ == "__main__":
    inicializar_banco()
    
    # Exemplo de uso:
    # 1. Cadastros
    cadastrar_cliente("João Silva", "joao@email.com")
    cadastrar_produto("Notebook", 3500.00, 5)
    
    # 2. Venda (Cliente ID 1 comprou 1 unidade do Produto ID 1)
    registrar_venda(1, 1, 1)
    
    # 3. Mostrar resultados
    ver_vendas()
