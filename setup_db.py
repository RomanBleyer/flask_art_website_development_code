import sqlite3
import os
import random

def create_database():
    """Create the missing artworks database with the products table."""
    
    # Remove existing database if it exists
    if os.path.exists('missing_artworks.db'):
        os.remove('missing_artworks.db')
        print("Existing database removed.")
    
    # Create new database connection
    conn = sqlite3.connect('missing_artworks.db')
    cursor = conn.cursor()
    
    # Create products table
    cursor.execute('''
        CREATE TABLE products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            image TEXT NOT NULL,
            name TEXT NOT NULL,
            price REAL NOT NULL,
            date_missing TEXT NOT NULL,
            original_artist TEXT NOT NULL,
            seller TEXT NOT NULL,
            description TEXT NOT NULL,
            painting_orientation TEXT NOT NULL CHECK (painting_orientation IN ('landscape', 'portrait', 'square')),
            stock INTEGER NOT NULL DEFAULT 1
        )
    ''')
    
    print("Database 'missing_artworks.db' created successfully!")
    print("Products table created with schema:")
    print("- id, image, name, price, date_missing, original_artist, seller, description, painting_orientation, stock")
    
    return conn

def populate_database(conn):
    """Populate the database with stolen artwork data."""
    
    cursor = conn.cursor()
    
    # Sample artwork data extracted from the images
    artworks = [
        {
            'image': 'infante_and_dog.jpg',
            'name': 'Infante and Dog',
            'price': 1000000,
            'date_missing': 'May 15, 1970',
            'original_artist': 'Diego Velázquez',
            'description': 'This is a description. It is very awesome and it will describe things till the end of TIME!!!',
            'painting_orientation': 'portrait',
            'stock': 1
        },
        {
            'image': 'landscape_cottages.jpg',
            'name': 'Landscape with Cottages',
            'price': 5000000,
            'date_missing': 'September 4, 1972',
            'original_artist': 'Rembrandt van Rijn',
            'description': 'This is a description. It is very awesome and it will describe things till the end of TIME!!!',
            'painting_orientation': 'landscape',
            'stock': 1
        },
        {
            'image': 'still_life_vanitas.jpg',
            'name': 'Still Life: Vanitas',
            'price': 2000000,
            'date_missing': 'September 4, 1972',
            'original_artist': 'Jan Davidsz van Heem',
            'description': 'This is a description. It is very awesome and it will describe things till the end of TIME!!!',
            'painting_orientation': 'square',
            'stock': 1
        },
        {
            'image': 'the_concert.jpg',
            'name': 'The Concert',
            'price': 200000000,
            'date_missing': 'March 18, 1990',
            'original_artist': 'Johannes Vermeer',
            'description': 'This is a description. It is very awesome and it will describe things till the end of TIME!!!',
            'painting_orientation': 'landscape',
            'stock': 1
        },
        {
            'image': 'storm_sea_galilee.jpg',
            'name': 'The Storm on the Sea of Galilee',
            'price': 100000000,
            'date_missing': 'March 18, 1990',
            'original_artist': 'Rembrandt van Rijn',
            'description': 'This is a description. It is very awesome and it will describe things till the end of TIME!!!',
            'painting_orientation': 'landscape',
            'stock': 1
        },
        {
            'image': 'landscape_obelisk.jpg',
            'name': 'Landscape with an Obelisk',
            'price': 5000000,
            'date_missing': 'March 18, 1990',
            'original_artist': 'Govert Flinck',
            'description': 'This is a description. It is very awesome and it will describe things till the end of TIME!!!',
            'painting_orientation': 'landscape',
            'stock': 1
        },
        {
            'image': 'man_with_pipe.jpg',
            'name': 'Man with a Pipe',
            'price': 2000000,
            'date_missing': '1998',
            'original_artist': 'Jean Metzinger',
            'description': 'This is a description. It is very awesome and it will describe things till the end of TIME!!!',
            'painting_orientation': 'portrait',
            'stock': 1
        },
        {
            'image': 'chemin_sevres.jpg',
            'name': 'Le chemin de Sèvres',
            'price': 1300000,
            'date_missing': 'May 3, 1998',
            'original_artist': 'Jean-Baptiste-Camille Corot',
            'description': 'This is a description. It is very awesome and it will describe things till the end of TIME!!!',
            'painting_orientation': 'landscape',
            'stock': 1
        },
        {
            'image': 'view_auvers.jpg',
            'name': 'View of Auvers-sur-Oise',
            'price': 10000000,
            'date_missing': 'December 31, 1999',
            'original_artist': 'Paul Cézanne',
            'description': 'This is a description. It is very awesome and it will describe things till the end of TIME!!!',
            'painting_orientation': 'landscape',
            'stock': 1
        },
        {
            'image': 'cavalier.jpg',
            'name': 'A Cavalier',
            'price': 1000000,
            'date_missing': 'June 10, 2007',
            'original_artist': 'Frans van Mieris the Elder',
            'description': 'This is a description. It is very awesome and it will describe things till the end of TIME!!!',
            'painting_orientation': 'portrait',
            'stock': 1
        },
        {
            'image': 'venus_mirror.jpg',
            'name': 'Venus with a Mirror',
            'price': 1000000,
            'date_missing': 'February 11, 2010',
            'original_artist': 'Jacopo Palma il Giovane',
            'description': 'This is a description. It is very awesome and it will describe things till the end of TIME!!!',
            'painting_orientation': 'portrait',
            'stock': 1
        },
        {
            'image': 'poppy_flowers.jpg',
            'name': 'Poppy Flowers',
            'price': 55000000,
            'date_missing': 'August 2010',
            'original_artist': 'Vincent van Gogh',
            'description': 'This is a description. It is very awesome and it will describe things till the end of TIME!!!',
            'painting_orientation': 'portrait',
            'stock': 1
        },
        {
            'image': 'madeleine_elbow.jpg',
            'name': 'Madeleine Leaning on her Elbow with Flowers in her Hair',
            'price': 1000000,
            'date_missing': 'September 8, 2011',
            'original_artist': 'Pierre-Auguste Renoir',
            'description': 'This is a description. It is very awesome and it will describe things till the end of TIME!!!',
            'painting_orientation': 'portrait',
            'stock': 1
        },
        {
            'image': 'soldier_horseback.jpg',
            'name': 'A Soldier on Horseback',
            'price': 3000000,
            'date_missing': 'March 14, 2020',
            'original_artist': 'Anthony van Dyck',
            'description': 'This is a description. It is very awesome and it will describe things till the end of TIME!!!',
            'painting_orientation': 'portrait',
            'stock': 1
        },
        {
            'image': 'boy_drinking.jpg',
            'name': 'A Boy Drinking',
            'price': 2000000,
            'date_missing': 'March 14, 2020',
            'original_artist': 'Annibale Carracci',
            'description': 'This is a description. It is very awesome and it will describe things till the end of TIME!!!',
            'painting_orientation': 'portrait',
            'stock': 1
        },
        {
            'image': 'nativity_francis.jpg',
            'name': 'Nativity with St. Francis and St. Lawrence',
            'price': 20000000,
            'date_missing': 'October 16, 1969',
            'original_artist': 'Caravaggio',
            'description': 'This is a description. It is very awesome and it will describe things till the end of TIME!!!',
            'painting_orientation': 'portrait',
            'stock': 1
        },
        {
            'image': 'pigeon_pois.jpg',
            'name': 'Le pigeon aux petits pois',
            'price': 28000000,
            'date_missing': 'May 20, 2010',
            'original_artist': 'Pablo Picasso',
            'description': 'This is a description. It is very awesome and it will describe things till the end of TIME!!!',
            'painting_orientation': 'square',
            'stock': 1
        },
        {
            'image': 'just_judges.jpg',
            'name': 'The Just Judges',
            'price': 50000000,
            'date_missing': 'April 10, 1934',
            'original_artist': 'Jan van Eyck',
            'description': 'This is a description. It is very awesome and it will describe things till the end of TIME!!!',
            'painting_orientation': 'portrait',
            'stock': 1
        },
        {
            'image': 'waterloo_bridge.jpg',
            'name': 'Waterloo Bridge, London',
            'price': 15000000,
            'date_missing': 'October 15-16, 2012',
            'original_artist': 'Claude Monet',
            'description': 'Presumably burnt by an accomplice during Kunsthal museum theft in Rotterdam.',
            'painting_orientation': 'landscape',
            'stock': 1
        },
        {
            'image': 'charing_cross.jpg',
            'name': 'Charing Cross Bridge, London',
            'price': 15000000,
            'date_missing': 'October 15-16, 2012',
            'original_artist': 'Claude Monet',
            'description': 'Presumably burnt by an accomplice during Kunsthal museum theft in Rotterdam.',
            'painting_orientation': 'landscape',
            'stock': 1
        },
        {
            'image': 'girl_window.jpg',
            'name': 'Girl in Front of Open Window',
            'price': 20000000,
            'date_missing': 'October 15-16, 2012',
            'original_artist': 'Paul Gauguin',
            'description': 'This is a description. It is very awesome and it will describe things till the end of TIME!!!',
            'painting_orientation': 'portrait',
            'stock': 1
        },
        {
            'image': 'self_portrait_haan.jpg',
            'name': 'Self-Portrait',
            'price': 10000000,
            'date_missing': 'October 15-16, 2012',
            'original_artist': 'Meyer de Haan',
            'description': 'This is a description. It is very awesome and it will describe things till the end of TIME!!!',
            'painting_orientation': 'portrait',
            'stock': 1
        },
        {
            'image': 'painter_work.jpg',
            'name': 'The Painter on His Way to Work',
            'price': 100000000,
            'date_missing': '1945',
            'original_artist': 'Vincent van Gogh',
            'description': 'This is a description. It is very awesome and it will describe things till the end of TIME!!!',
            'painting_orientation': 'portrait',
            'stock': 1
        },
        {
            'image': 'portrait_young_man.jpg',
            'name': 'Portrait of a Young Man',
            'price': 100000000,
            'date_missing': '1940s',
            'original_artist': 'Raphael',
            'description': 'This is a description. It is very awesome and it will describe things till the end of TIME!!!',
            'painting_orientation': 'portrait',
            'stock': 1
        },
        {
            'image': 'en_canot.jpg',
            'name': 'En Canot',
            'price': 2400000,
            'date_missing': 'c. 1936',
            'original_artist': 'Jean Metzinger',
            'description': 'This is a description. It is very awesome and it will describe things till the end of TIME!!!',
            'painting_orientation': 'landscape',
            'stock': 1
        },
        {
            'image': 'allegory_belief.jpg',
            'name': 'Allegory of Christian Belief',
            'price': 5000000,
            'date_missing': '1939',
            'original_artist': 'Johann Liss',
            'description': 'This is a description. It is very awesome and it will describe things till the end of TIME!!!',
            'painting_orientation': 'portrait',
            'stock': 1
        },
        {
            'image': 'young_couple.jpg',
            'name': 'Young Couple in a Landscape',
            'price': 3000000,
            'date_missing': '1939',
            'original_artist': 'Georg Penz',
            'description': 'This is a description. It is very awesome and it will describe things till the end of TIME!!!',
            'painting_orientation': 'landscape',
            'stock': 1
        }
    ]
    
    # Insert each artwork into the database
    for artwork in artworks:
        # Randomly assign seller (50/50 John Doe vs Jane Doe)
        seller = random.choice(['John Doe', 'Jane Doe'])
        artwork['seller'] = seller
        
        cursor.execute('''
            INSERT INTO products (image, name, price, date_missing, original_artist, seller, description, painting_orientation, stock)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            artwork['image'],
            artwork['name'], 
            artwork['price'],
            artwork['date_missing'],
            artwork['original_artist'],
            artwork['seller'],
            artwork['description'],
            artwork['painting_orientation'],
            artwork['stock']
        ))
    
    print(f"Successfully added {len(artworks)} stolen artworks to the database!")
    print("Your missing masterpieces marketplace is now fully stocked!")
    
    return len(artworks)

def main():
    """Main function to set up and populate the database."""
    try:
        # Create database and table
        conn = create_database()
        
        # Populate with artwork data
        artwork_count = populate_database(conn)
        
        # Commit changes and close connection
        conn.commit()
        conn.close()
        
        print(f"\n=== DATABASE SETUP COMPLETE ===")
        print(f"Database: missing_artworks.db")
        print(f"Total artworks: {artwork_count}")
        print(f"Ready to launch your missing masterpieces marketplace! 🎨💰")
        
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    main()