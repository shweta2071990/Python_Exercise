import sqlite3
import math

# ------------------------------
# Database Setup
# ------------------------------
def init_db():
    conn = sqlite3.connect("cities.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS city_coordinates (
            city TEXT PRIMARY KEY,
            latitude REAL,
            longitude REAL
        )
    """)
    conn.commit()
    return conn


# ------------------------------
# Helper: Fetch coordinates
# ------------------------------
def get_city_coordinates(conn, city_name):
    cursor = conn.cursor()
    cursor.execute("SELECT latitude, longitude FROM city_coordinates WHERE city = ?", (city_name.lower(),))
    result = cursor.fetchone()

    if result:
        return result  # (lat, lon)

    # If city not found → ask user
    print(f"\nI don't have coordinates for '{city_name}'. Please enter them:")
    lat = float(input("  Enter latitude  : "))
    lon = float(input("  Enter longitude : "))

    cursor.execute(
        "INSERT INTO city_coordinates (city, latitude, longitude) VALUES (?, ?, ?)",
        (city_name.lower(), lat, lon)
    )
    conn.commit()

    return lat, lon


# ------------------------------
# Haversine Distance in KM
# ------------------------------
def haversine(lat1, lon1, lat2, lon2):
    R = 6371.0  # Earth radius in km

    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = math.sin(dlat/2)**2 + math.cos(lat1)*math.cos(lat2)*math.sin(dlon/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    return R * c


# ------------------------------
# Main Program
# ------------------------------
def main():
    conn = init_db()

    print("\n=== Straight-Line Distance Between Cities ===")

    city1 = input("\nEnter first city name  : ").strip()
    city2 = input("Enter second city name : ").strip()

    lat1, lon1 = get_city_coordinates(conn, city1)
    lat2, lon2 = get_city_coordinates(conn, city2)

    distance_km = haversine(lat1, lon1, lat2, lon2)

    print(f"\n📍 Straight-line distance between **{city1}** and **{city2}**: {distance_km:.2f} km\n")

    conn.close()


if __name__ == "__main__":
    main()