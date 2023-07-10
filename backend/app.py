import os
import base64
import tensorflow as tf
from tensorflow.keras.preprocessing import image
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)
app.config['UPLOAD_FOLDER'] = 'uploads'
model = tf.keras.models.load_model('EfficientNetB4-INSECTS-0.00.h5')
image_size = (200, 200)


@app.route('/predict', methods=['POST'])
def predict():
    image_data = request.get_json().get('image_data')
    if image_data:
        image_data = image_data.replace('data:image/png;base64,', '')
        image_data = base64.b64decode(image_data)
        image_path = os.path.join(app.config['UPLOAD_FOLDER'], 'capture.png')
        with open(image_path, 'wb') as f:
            f.write(image_data)
        img = image.load_img(image_path, target_size=image_size)
        img = image.img_to_array(img)
        # img = tf.expand_dims(img, axis=0) / 255.0
        img = tf.expand_dims(img, axis=0)
        prediction = model.predict(img)
        class_index = prediction.argmax()
        pest_list = [
            "rice leaf roller",
            "rice leaf caterpillar",
            "paddy stem maggot",
            "asiatic rice borer",
            "yellow rice borer",
            "rice gall midge",
            "Rice Stemfly",
            "brown plant hopper",
            "white backed plant hopper",
            "small brown plant hopper",
            "rice water weevil",
            "rice leafhopper",
            "grain spreader thrips",
            "rice shell pest",
            "grub",
            "mole cricket",
            "wireworm",
            "white margined moth",
            "black cutworm",
            "large cutworm",
            "yellow cutworm",
            "red spider",
            "corn borer",
            "army worm",
            "aphids",
            "Potosiabre vitarsis",
            "peach borer",
            "english grain aphid",
            "green bug",
            "bird cherry-oataphid",
            "wheat blossom midge",
            "penthaleus major",
            "longlegged spider mite",
            "wheat phloeothrips",
            "wheat sawfly",
            "cerodonta denticornis",
            "beet fly",
            "flea beetle",
            "cabbage army worm",
            "beet army worm",
            "Beet spot flies",
            "meadow moth",
            "beet weevil",
            "sericaorient alismots chulsky",
            "alfalfa weevil",
            "flax budworm",
            "alfalfa plant bug",
            "tarnished plant bug",
            "Locustoidea",
            "lytta polita",
            "legume blister beetle",
            "blister beetle",
            "therioaphis maculata Buckton",
            "odontothrips loti",
            "Thrips",
            "alfalfa seed chalcid",
            "Pieris canidia",
            "Apolygus lucorum",
            "Limacodidae",
            "Viteus vitifoliae",
            "Colomerus vitis",
            "Brevipoalpus lewisi McGregor",
            "oides decempunctata",
            "Polyphagotars onemus latus",
            "Pseudococcus comstocki Kuwana",
            "parathrene regalis",
            "Ampelophaga",
            "Lycorma delicatula",
            "Xylotrechus",
            "Cicadella viridis",
            "Miridae",
            "Trialeurodes vaporariorum",
            "Erythroneura apicalis",
            "Papilio xuthus",
            "Panonchus citri McGregor",
            "Phyllocoptes oleiverus ashmead",
            "Icerya purchasi Maskell",
            "Unaspis yanonensis",
            "Ceroplastes rubens",
            "Chrysomphalus aonidum",
            "Parlatoria zizyphus Lucus",
            "Nipaecoccus vastalor",
            "Aleurocanthus spiniferus",
            "Tetradacus c Bactrocera minax",
            "Dacus dorsalis(Hendel)",
            "Bactrocera tsuneonis",
            "Prodenia litura",
            "Adristyrannus",
            "Phyllocnistis citrella Stainton",
            "Toxoptera citricidus",
            "Toxoptera aurantii",
            "Aphis citricola Vander Goot",
            "Scirtothrips dorsalis Hood",
            "Dasineura sp",
            "Lawana imitata Melichar",
            "Salurnis marginella Guerr",
            "Deporaus marginatus Pascoe",
            "Chlumetia transversa",
            "Mango flat beak leafhopper",
            "Rhytidodera bowrinii white",
            "Sternochetus frigidus",
            "Cicadellidae"
        ]

        result = pest_list[class_index]
        # return jsonify({'prediction': result})
        response = jsonify({'prediction': result})
        return response
    response = jsonify({'prediction': 'Error: No image data'})
    return response


if __name__ == '__main__':
    app.run(debug=True)
