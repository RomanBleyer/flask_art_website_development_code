import sqlite3
import os
import random

def create_database():
    """Create the missing artworks database with comprehensive categorization."""
    
    # Remove existing database if it exists
    if os.path.exists('missing_artworks.db'):
        os.remove('missing_artworks.db')
        print("Existing database removed.")
    
    # Create new database connection
    conn = sqlite3.connect('missing_artworks.db')
    cursor = conn.cursor()
    
    # Create products table with all category fields
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
            
            -- Orientation categories
            orientation TEXT NOT NULL CHECK (orientation IN ('Landscape', 'Portrait', 'Square')),
            
            -- Price range categories  
            price_range TEXT NOT NULL CHECK (price_range IN ('0-5 mil', '5-20 mil', '20-50 mil', '50+ mil')),
            
            -- Date categories
            date_category TEXT NOT NULL CHECK (date_category IN ('1900 to 1950', '1950 to 1970', '1970 to 1990', '1990 to present')),
            
            -- Art movement categories
            art_movement TEXT NOT NULL CHECK (art_movement IN ('Renaissance', 'Baroque', 'Impressionism', 'Post-Impressionism', 'Cubism', 'Abstract', 'Modern', 'Contemporary', 'Classical')),
            
            -- Type of painting categories
            painting_type TEXT NOT NULL CHECK (painting_type IN ('Subject portrait', 'Landscape Rendition', 'Object portrait', 'Other')),
            
            stock INTEGER NOT NULL DEFAULT 1
        )
    ''')
    
    print("Database 'missing_artworks.db' created successfully!")
    print("Products table created with comprehensive categorization system")
    print("Categories: Orientation, Price Range, Date, Art Movement, Painting Type")
    
    return conn

def get_price_range(price):
    """Determine price range category based on price."""
    if price < 5000000:
        return '0-5 mil'
    elif price < 20000000:
        return '5-20 mil'
    elif price < 50000000:
        return '20-50 mil'
    else:
        return '50+ mil'

def get_date_category(date_missing):
    """Determine date category based on date missing."""
    if any(year in date_missing for year in ['1900', '1901', '1902', '1903', '1904', '1905', '1906', '1907', '1908', '1909', 
                                           '1910', '1911', '1912', '1913', '1914', '1915', '1916', '1917', '1918', '1919',
                                           '1920', '1921', '1922', '1923', '1924', '1925', '1926', '1927', '1928', '1929',
                                           '1930', '1931', '1932', '1933', '1934', '1935', '1936', '1937', '1938', '1939',
                                           '1940', '1941', '1942', '1943', '1944', '1945', '1946', '1947', '1948', '1949']):
        return '1900 to 1950'
    elif any(year in date_missing for year in ['1950', '1951', '1952', '1953', '1954', '1955', '1956', '1957', '1958', '1959',
                                             '1960', '1961', '1962', '1963', '1964', '1965', '1966', '1967', '1968', '1969']):
        return '1950 to 1970'
    elif any(year in date_missing for year in ['1970', '1971', '1972', '1973', '1974', '1975', '1976', '1977', '1978', '1979',
                                             '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989']):
        return '1970 to 1990'
    else:
        return '1990 to present'

def get_art_movement(artist, name):
    """Determine art movement based on artist and artwork name."""
    artist_lower = artist.lower()
    name_lower = name.lower()
    
    if any(artist_name in artist_lower for artist_name in ['van gogh', 'cézanne', 'gauguin']):
        return 'Post-Impressionism'
    elif any(artist_name in artist_lower for artist_name in ['monet', 'renoir']):
        return 'Impressionism'
    elif any(artist_name in artist_lower for artist_name in ['picasso', 'metzinger']):
        return 'Cubism'
    elif any(artist_name in artist_lower for artist_name in ['rembrandt', 'vermeer', 'van dyck']):
        return 'Baroque'
    elif any(artist_name in artist_lower for artist_name in ['raphael', 'caravaggio']):
        return 'Renaissance'
    elif any(artist_name in artist_lower for artist_name in ['velázquez', 'van eyck']):
        return 'Classical'
    else:
        return 'Modern'

def get_painting_type(name, description):
    """Determine painting type based on name and description."""
    name_lower = name.lower()
    desc_lower = description.lower()
    
    if any(word in name_lower for word in ['portrait', 'man', 'woman', 'boy', 'girl', 'cavalier', 'soldier', 'infante']):
        return 'Subject portrait'
    elif any(word in name_lower for word in ['landscape', 'view', 'bridge', 'storm', 'sea', 'cottages', 'obelisk']):
        return 'Landscape Rendition'
    elif any(word in name_lower for word in ['still life', 'flowers', 'poppy', 'vanitas', 'venus']):
        return 'Object portrait'
    else:
        return 'Other'

def populate_database(conn):
    """Populate the database with categorized stolen artwork data."""
    
    cursor = conn.cursor()
    
    # Sample artwork data - will be auto-categorized
    artworks = [
        {
            'image': 'infante_and_dog.jpg',
            'name': 'Infante and Dog',
            'price': 1000000,
            'date_missing': 'May 15, 1970',
            'original_artist': 'Diego Velázquez',
            'description': 'Stolen from a private residence during a burglary in Marseille, France.',
            'orientation': 'Portrait',
        },
        {
            'image': 'landscape_cottages.jpg',
            'name': 'Landscape with Cottages',
            'price': 5000000,
            'date_missing': 'September 4, 1972',
            'original_artist': 'Rembrandt van Rijn',
            'description': 'A rare Rembrandt landscape stolen from the Montreal Museum of Fine Arts by armed robbers.',
            'orientation': 'Landscape',
        },
        {
            'image': 'still_life_vanitas.jpg',
            'name': 'Still Life: Vanitas',
            'price': 2000000,
            'date_missing': 'September 4, 1972',
            'original_artist': 'Jan Davidsz van Heem',
            'description': 'Among paintings stolen from the Montreal Museum of Fine Arts by armed robbers.',
            'orientation': 'Square',
        },
        {
            'image': 'the_concert.jpg',
            'name': 'The Concert',
            'price': 200000000,
            'date_missing': 'March 18, 1990',
            'original_artist': 'Johannes Vermeer',
            'description': 'The most valuable stolen painting in the world. Stolen from Isabella Stewart Gardner Museum in Boston.',
            'orientation': 'Landscape',
        },
        {
            'image': 'storm_sea_galilee.jpg',
            'name': 'The Storm on the Sea of Galilee',
            'price': 100000000,
            'date_missing': 'March 18, 1990',
            'original_artist': 'Rembrandt van Rijn',
            'description': 'Rembrandt\'s only seascape, stolen from Isabella Stewart Gardner Museum.',
            'orientation': 'Landscape',
        },
        {
            'image': 'landscape_obelisk.jpg',
            'name': 'Landscape with an Obelisk',
            'price': 5000000,
            'date_missing': 'March 18, 1990',
            'original_artist': 'Govert Flinck',
            'description': 'Part of the Isabella Stewart Gardner Museum heist, attributed to Rembrandt student.',
            'orientation': 'Landscape',
        },
        {
            'image': 'man_with_pipe.jpg',
            'name': 'Man with a Pipe',
            'price': 2000000,
            'date_missing': '1998',
            'original_artist': 'Jean Metzinger',
            'description': 'Missing from Lawrence University, Wisconsin since 1998.',
            'orientation': 'Portrait',
        },
        {
            'image': 'chemin_sevres.jpg',
            'name': 'Le chemin de Sèvres',
            'price': 1300000,
            'date_missing': 'May 3, 1998',
            'original_artist': 'Jean-Baptiste-Camille Corot',
            'description': 'Stolen by visitor during open hours from The Louvre, Paris.',
            'orientation': 'Landscape',
        },
        {
            'image': 'view_auvers.jpg',
            'name': 'View of Auvers-sur-Oise',
            'price': 10000000,
            'date_missing': 'December 31, 1999',
            'original_artist': 'Paul Cézanne',
            'description': 'Stolen from Ashmolean Museum, Oxford during New Year\'s Eve celebrations.',
            'orientation': 'Landscape',
        },
        {
            'image': 'cavalier.jpg',
            'name': 'A Cavalier',
            'price': 1000000,
            'date_missing': 'June 10, 2007',
            'original_artist': 'Frans van Mieris the Elder',
            'description': 'Stolen by visitor during opening hours from Art Gallery of New South Wales, Sydney.',
            'orientation': 'Portrait',
        },
        {
            'image': 'venus_mirror.jpg',
            'name': 'Venus with a Mirror',
            'price': 1000000,
            'date_missing': 'February 11, 2010',
            'original_artist': 'Jacopo Palma il Giovane',
            'description': 'Stolen from Budapest Palace by robbers using force.',
            'orientation': 'Portrait',
        },
        {
            'image': 'poppy_flowers.jpg',
            'name': 'Poppy Flowers',
            'price': 55000000,
            'date_missing': 'August 2010',
            'original_artist': 'Vincent van Gogh',
            'description': 'Also known as Vase and Flowers. Stolen from Mohammed Mahmoud Khalil Museum, Cairo.',
            'orientation': 'Portrait',
        },
        {
            'image': 'madeleine_elbow.jpg',
            'name': 'Madeleine Leaning on her Elbow with Flowers in her Hair',
            'price': 1000000,
            'date_missing': 'September 8, 2011',
            'original_artist': 'Pierre-Auguste Renoir',
            'description': 'Stolen by armed robber at night from private residence in Houston, Texas.',
            'orientation': 'Portrait',
        },
        {
            'image': 'soldier_horseback.jpg',
            'name': 'A Soldier on Horseback',
            'price': 3000000,
            'date_missing': 'March 14, 2020',
            'original_artist': 'Anthony van Dyck',
            'description': 'Stolen at night along with two other paintings from Christ Church Picture Gallery, Oxford.',
            'orientation': 'Portrait',
        },
        {
            'image': 'boy_drinking.jpg',
            'name': 'A Boy Drinking',
            'price': 2000000,
            'date_missing': 'March 14, 2020',
            'original_artist': 'Annibale Carracci',
            'description': 'Stolen at night along with two other paintings from Christ Church Picture Gallery, Oxford.',
            'orientation': 'Portrait',
        },
        {
            'image': 'nativity_francis.jpg',
            'name': 'Nativity with St. Francis and St. Lawrence',
            'price': 20000000,
            'date_missing': 'October 16, 1969',
            'original_artist': 'Caravaggio',
            'description': 'Stolen from San Lorenzo in Palermo, Sicily. Large painting measuring almost six square metres.',
            'orientation': 'Portrait',
        },
        {
            'image': 'pigeon_pois.jpg',
            'name': 'Le pigeon aux petits pois',
            'price': 28000000,
            'date_missing': 'May 20, 2010',
            'original_artist': 'Pablo Picasso',
            'description': 'One of five paintings stolen from Musée d\'Art Moderne de la Ville de Paris.',
            'orientation': 'Square',
        },
        {
            'image': 'just_judges.jpg',
            'name': 'The Just Judges',
            'price': 50000000,
            'date_missing': 'April 10, 1934',
            'original_artist': 'Jan van Eyck',
            'description': 'Lower left panel of the Ghent Altarpiece, stolen from Saint Bavo Cathedral in Belgium.',
            'orientation': 'Portrait',
        },
        {
            'image': 'waterloo_bridge.jpg',
            'name': 'Waterloo Bridge, London',
            'price': 15000000,
            'date_missing': 'October 15-16, 2012',
            'original_artist': 'Claude Monet',
            'description': 'Presumably burnt by an accomplice during Kunsthal museum theft in Rotterdam.',
            'orientation': 'Landscape',
        },
        {
            'image': 'charing_cross.jpg',
            'name': 'Charing Cross Bridge, London',
            'price': 15000000,
            'date_missing': 'October 15-16, 2012',
            'original_artist': 'Claude Monet',
            'description': 'Presumably burnt by an accomplice during Kunsthal museum theft in Rotterdam.',
            'orientation': 'Landscape',
        },
        {
            'image': 'girl_window.jpg',
            'name': 'Girl in Front of Open Window',
            'price': 20000000,
            'date_missing': 'October 15-16, 2012',
            'original_artist': 'Paul Gauguin',
            'description': 'Also known as La Francée. Presumably burnt by an accomplice during Kunsthal theft.',
            'orientation': 'Portrait',
        },
        {
            'image': 'self_portrait_haan.jpg',
            'name': 'Self-Portrait',
            'price': 10000000,
            'date_missing': 'October 15-16, 2012',
            'original_artist': 'Meyer de Haan',
            'description': 'Presumably burnt by an accomplice during Kunsthal museum theft in Rotterdam.',
            'orientation': 'Portrait',
        },
        {
            'image': 'painter_work.jpg',
            'name': 'The Painter on His Way to Work',
            'price': 100000000,
            'date_missing': '1945',
            'original_artist': 'Vincent van Gogh',
            'description': 'Listed as missing from Stassfurt salt mines art repository near Magdeburg, Germany.',
            'orientation': 'Portrait',
        },
        {
            'image': 'portrait_young_man.jpg',
            'name': 'Portrait of a Young Man',
            'price': 100000000,
            'date_missing': '1940s',
            'original_artist': 'Raphael',
            'description': 'Plundered by the Nazis in Poland. Many scholars regard it as Raphael\'s self-portrait.',
            'orientation': 'Portrait',
        },
        {
            'image': 'en_canot.jpg',
            'name': 'En Canot',
            'price': 2400000,
            'date_missing': 'c. 1936',
            'original_artist': 'Jean Metzinger',
            'description': 'Confiscated by the Nazis and has been missing ever since.',
            'orientation': 'Landscape',
        },
        {
            'image': 'allegory_belief.jpg',
            'name': 'Allegory of Christian Belief',
            'price': 5000000,
            'date_missing': '1939',
            'original_artist': 'Johann Liss',
            'description': 'Nazi Gestapo confiscated roughly 750 Old Master drawings from Jewish collector.',
            'orientation': 'Portrait',
        },
        {
            'image': 'young_couple.jpg',
            'name': 'Young Couple in a Landscape',
            'price': 3000000,
            'date_missing': '1939',
            'original_artist': 'Georg Penz',
            'description': 'Nazi Gestapo confiscated roughly 750 Old Master drawings from Jewish collector.',
            'orientation': 'Landscape',
        }
    ]
    
    # Insert each artwork with auto-categorization
    for artwork in artworks:
        seller = random.choice(['John Doe', 'Jane Doe'])
        price_range = get_price_range(artwork['price'])
        date_category = get_date_category(artwork['date_missing'])
        art_movement = get_art_movement(artwork['original_artist'], artwork['name'])
        painting_type = get_painting_type(artwork['name'], artwork['description'])
        
        cursor.execute('''
            INSERT INTO products (image, name, price, date_missing, original_artist, seller, description, 
                                orientation, price_range, date_category, art_movement, painting_type, stock)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            artwork['image'],
            artwork['name'], 
            artwork['price'],
            artwork['date_missing'],
            artwork['original_artist'],
            seller,
            artwork['description'],
            artwork['orientation'],
            price_range,
            date_category,
            art_movement,
            painting_type,
            1
        ))
    
    print(f"Successfully added {len(artworks)} categorized stolen artworks to the database!")
    print("Categories applied: Orientation, Price Range, Date, Art Movement, Painting Type")
    
    return len(artworks)

def main():
    """Main function to set up and populate the categorized database."""
    try:
        # Create database and table
        conn = create_database()
        
        # Populate with categorized artwork data
        artwork_count = populate_database(conn)
        
        # Commit changes and close connection
        conn.commit()
        conn.close()
        
        print(f"\n=== CATEGORIZED DATABASE SETUP COMPLETE ===")
        print(f"Database: missing_artworks.db")
        print(f"Total artworks: {artwork_count}")
        print(f"5 Category types implemented:")
        print(f"- Orientation: Landscape, Portrait, Square")
        print(f"- Price Range: 0-5 mil, 5-20 mil, 20-50 mil, 50+ mil")
        print(f"- Date: 1900-1950, 1950-1970, 1970-1990, 1990-present")
        print(f"- Art Movement: Renaissance, Baroque, Impressionism, etc.")
        print(f"- Painting Type: Subject portrait, Landscape Rendition, etc.")
        print(f"Ready to launch your fully categorized marketplace! 🎨💰")
        
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    main()