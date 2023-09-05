import mysql.connector
from decouple import config

# Establish a connection to the database
conn = mysql.connector.connect(
    user=config("MYSQL_USER"), password=config("MYSQL_PASSWORD"), host="127.0.0.1"
)
cur = conn.cursor()

# Define table creation queries
cur.execute("CREATE DATABASE IF NOT EXISTS discord_clone_db")
cur.execute("USE discord_clone_db")

user = """CREATE table IF NOT EXISTS users(
    user_id INT NOT NULL AUTO_INCREMENT UNIQUE PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    password_digest VARCHAR(255) NOT NULL,
    email VARCHAR(120),
    creation_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP(),
    image VARCHAR(45)
)"""

server = """CREATE table IF NOT EXISTS servers(
    server_id INT NOT NULL AUTO_INCREMENT UNIQUE PRIMARY KEY,
    server_name VARCHAR(50) NOT NULL,
    server_description VARCHAR(255),
    creation_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP(),
    owner_id INT NOT NULL,
    FOREIGN KEY (owner_id) REFERENCES users (user_id) ON DELETE CASCADE
)"""

user_servers = """CREATE table IF NOT EXISTS user_servers(
    user_server_id INT NOT NULL AUTO_INCREMENT UNIQUE PRIMARY KEY,
    user_id INT NOT NULL,
    server_id INT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users (user_id) ON DELETE CASCADE,
    FOREIGN KEY (server_id) REFERENCES servers (server_id)
)"""

channels = """CREATE table IF NOT EXISTS channels(
    channel_id INT NOT NULL AUTO_INCREMENT UNIQUE PRIMARY KEY,
    channel_name VARCHAR(50) NOT NULL,
    user_id INT NOT NULL,
    server_id INT NOT NULL,
    creation_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP(),
    FOREIGN KEY (user_id) REFERENCES users (user_id),
    FOREIGN KEY (server_id) REFERENCES servers (server_id) ON DELETE CASCADE
)"""

messages = """CREATE table IF NOT EXISTS messages(
    message_id INT NOT NULL AUTO_INCREMENT UNIQUE PRIMARY KEY,
    message_body VARCHAR(255) NOT NULL,
    user_id INT NOT NULL,
    channel_id INT NOT NULL,
    creation_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP(),
    update_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP(),
    FOREIGN KEY (user_id) REFERENCES users (user_id) ON DELETE CASCADE,
    FOREIGN KEY (channel_id) REFERENCES channels (channel_id) ON DELETE CASCADE
)"""

tables = [user, server, user_servers, channels, messages]

for table in tables:
    cur.execute(table)

conn.commit()
conn.close()
