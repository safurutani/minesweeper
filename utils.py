import settings

def height_percent(percentage):
    return (settings.HEIGHT / 100) * percentage
print(height_percent(25))