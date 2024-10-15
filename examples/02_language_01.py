# Simplest command form: <multiplier><motion>

# Motion commands:
# - h j k l     --> left up down right
# - gg G        --> go to top / bottom of the file
# - w           --> go to next word
# - b e         --> go to beginning / end of the word
# - ^ $         --> go to beginning / end of the line

company_name = "Zeiss"
list_of_locations = ["Aalen", "Jena", "Oberkochen"]

for location in list_of_locations:
    print(f"{company_name} has a location in {location}")


# 02_language_02.py