import random
from data.persons import persons
from data.themes import themes
from data.artists import artists
from data.theme_artists import theme_artists

# Define multiple templates
templates = [
    "A {descriptor} cybersecurity landscape, featuring {primary} with {modifier}, including {additional_elements}, illuminated by {lighting_effects}, evoking a {mood} mood, {architectural_elements}, set in {context} with a {style} aesthetic and {texture_effects}.",
    "{artist_styles}, {descriptor} network showcasing {primary} enhanced by {modifier}, including {additional_elements}, illuminated by {lighting_effects}, evoking a {mood} mood, and incorporating {architectural_elements} within a {style} framework. {texture_effects}",
    "{context}, {artist_styles}, a {descriptor} scene featuring {primary} with {modifier}, including {additional_elements}, illuminated by {lighting_effects}, creating a {mood} atmosphere and featuring {architectural_elements} in a {style} style with {texture_effects}.",
    "{artist_styles}, {descriptor} elements like {primary} intertwine with {modifier}, including {additional_elements}, illuminated by {lighting_effects}, creating a {mood} ambiance, featuring {architectural_elements}, set in {context} with a {style} aesthetic and {texture_effects}."
]


def select_artists(associated_artists, artists_dict, max_artists=2, max_styles=2):
    """Selects a random number of styles and combines their descriptors."""
    num_artists = random.randint(1, max_artists)
    selected_artists = random.sample(
        associated_artists, k=min(num_artists, len(associated_artists))
    )
    print(selected_artists)

    style_descriptors = []
    for artist in selected_artists:
        styles = artists_dict.get(artist, ["unique style"])
        style_descriptors.extend(styles)

    # shuffle styles_descriptors
    random.shuffle(style_descriptors)

    # limit styles_descriptors to max_styles
    style_descriptors = style_descriptors[:max_styles]

    print(style_descriptors)

    artist_styles = ", ".join(style_descriptors)
    return artist_styles


def generate_prompt(theme_name):
    theme = themes.get(theme_name)
    if not theme:
        return f"Theme '{theme_name}' not found."

    # Select keywords from theme
    descriptor = random.choice(theme["descriptors"])
    primary = random.choice(theme["primary_elements"])
    modifier = random.choice(theme["modifiers"])
    context = random.choice(theme["context"])
    mood = random.choice(theme["mood"])
    architectural_element = random.choice(theme["architectural_elements"])
    style = random.choice(theme["style"])
    additional_elements = random.choice(theme["additional_elements"])
    lighting_effects = random.choice(theme["lighting_effects"])
    texture_effects = random.choice(theme["texture_effects"])

    # Select artists associated with the theme
    associated_artists = theme_artists.get(theme_name, [])
    if associated_artists:
        artist_styles = select_artists(associated_artists, artists)
    else:
        artist_styles = "styled with a unique artistic style"

    # Select a template
    template = random.choice(templates)
    print(template)

    # Format prompt
    prompt = template.format(
        descriptor=descriptor,
        primary=primary,
        modifier=modifier,
        context=context,
        mood=mood,
        architectural_elements=architectural_element,
        style=style,
        additional_elements=additional_elements,
        lighting_effects=lighting_effects,
        texture_effects=texture_effects,
        artist_styles=artist_styles,
    )

    return prompt


def list_themes():
    print("Available Themes:")
    for idx, theme in enumerate(themes.keys(), 1):
        print(f"{idx}. {theme}")


def main():
    while True:
        print("\n--- Prompt Generator ---")
        list_themes()
        print("0. Exit")
        try:
            choice = int(input("\nSelect a theme by number: "))
            if choice == 0:
                print("Exiting...")
                break
            elif 1 <= choice <= len(themes):
                theme_name = list(themes.keys())[choice - 1]
                prompt = generate_prompt(theme_name)
                print(f"\nGenerated Prompt for '{theme_name}':\n{prompt}\n")
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Please enter a valid number.")


if __name__ == "__main__":
    main()
