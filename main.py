import pendulum
if __name__ == '__main__':
    now = pendulum.now("Europe/Paris")
    # Changing timezone
    print(now.in_timezone("America/Toronto"))
    # Default support for common datetime formats
    print(now.to_iso8601_string())
    # Shifting
    print(now.add(days=2))
    print(now)
