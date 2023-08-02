# Assuming the database connection has been established
cursor = db.cursor()

# Define the memory
memory = {
    "title": "Playing House with Anna",
    "identifier": 2,
    "date": "1998-05-12",
    "people": ["Mary", "Anna", "Mom"],
    "triggers": ["playing house", "Anna", "Mother", "teaching"],
    "text": "Anna and I had a long argument about who gets to be the mom while playing house. Mother overheard us and gently explained that being a mother is not about being bossy or wearing the prettiest clothes, but about loving and caring for your family. This meaningful talk had a profound impact on both Anna and me."
}

# Insert the memory into the database
insert_into_table(cursor, "Memories", memory)

# Don't forget to commit your changes and close the connection when you're done!
db.commit()
db.close()
