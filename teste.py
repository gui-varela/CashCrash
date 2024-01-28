from faker import Faker

# Crie uma instância do Faker
fake = Faker()

# Gere um ID fictício simples usando um número aleatório
id_ficticio = fake.random_int(min=1, max=100000)

print(f"ID fictício: {id_ficticio}")
