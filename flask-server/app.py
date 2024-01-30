from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/generate_comic', methods=['POST'])
def generate_comic():
    import json
    from generate_panels import generate_panels
    from stability_ai import text_to_image
    from add_text import add_text_to_panel
    from create_strip import create_strip
    data = request.get_json()
    scenario = data['scenario']
    style = data['style']

    panels = generate_panels(scenario)

    with open('output/panels.json', 'w') as outfile:
        json.dump(panels, outfile)

    panel_images = []

    for panel in panels:
        panel_prompt = panel["description"] + ", cartoon box, " + style
        print(f"Generate panel {panel['number']} with prompt: {panel_prompt}")
        panel_image = text_to_image(panel_prompt)
        panel_image_with_text = add_text_to_panel(panel["text"], panel_image)
        panel_images.append(panel_image_with_text)

    create_strip(panel_images).save("output/strip.png")

    return jsonify({'success': True, 'message': 'Comic generated successfully'})
    console.log("Output created")
if __name__ == '__main__':
    app.run(port=5000)
