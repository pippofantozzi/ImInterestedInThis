
text = """What is Physics-Informed Machine Learning?
PIML is a cutting-edge approach that integrates physical laws into the training of machine learning models. Unlike traditional machine learning models that learn solely from data, PIML models are informed by the underlying physics of the problem, which guides the learning process. This synergy between data and physics opens up new avenues for solving scientific and engineering challenges.

The Benefits of Physics-Informed Machine Learning
1. Reduced Data Dependency: PIML models require significantly less data to train because they leverage known physical laws, making them ideal for scenarios where data collection is expensive or challenging.
2. Enhanced Predictive Performance: By incorporating physical principles, these models make predictions that are more accurate and physically plausible, reducing the risk of unrealistic results.
3. Generalizability: PIML models can generalize better to unseen conditions by adhering to physical laws, making them more robust and reliable.
4. Efficiency: They can significantly reduce computational costs and time, as they converge to solutions faster by navigating the solution space more effectively.

Applications and Impact
The applications of PIML span across various fields, from fluid dynamics to materials science, and from climate modeling to biomedical engineering. Here are a few exhilarating case studies:
1. Predicting Turbulent Flows: In fluid dynamics, PIML has been used to predict turbulent flows more accurately than traditional computational fluid dynamics models, showcasing its potential to revolutionize aerospace and mechanical engineering designs.
2. Material Discovery: In materials science, PIML has accelerated the discovery of new materials with desired properties by efficiently navigating the vast design space, which is a game-changer for industries ranging from electronics to pharmaceuticals.
3. Climate Modeling: PIML models have improved the accuracy of climate predictions by better capturing complex physical interactions in the atmosphere, offering new insights into climate change mitigation strategies.

The Future of Physics-Informed Machine Learning
The future of PIML is boundless. As we continue to unravel the potential of this interdisciplinary field, we can anticipate groundbreaking advancements in scientific research and technology development. From enabling more efficient renewable energy systems to advancing precision medicine, the impact of PIML will be far-reaching.

Look Ahead
Imagine a world where we can predict natural disasters with greater accuracy, design more effective drugs faster, and develop sustainable technologies more efficiently. PIML stands at the forefront of this new era, bridging the gap between theoretical physics and practical applications.

Conclusion
In conclusion, Physics-Informed Machine Learning is not just a novel approach to problem-solving; it's a paradigm shift that redefines the boundaries of what's possible. As we venture further into this uncharted territory, let's embrace the challenges and opportunities it presents, forging a future where the synergy between physics and AI transforms our world for the better.

Thank you for your attention. Let's continue to explore, innovate, and inspire, as we pave the way for a brighter, more informed future.
"""

def process_text(input_text=text):
    lines = input_text.split('\n')
    subheaders = []
    texts = []
    bullets = []
    current_text = ""
    expecting_subheader = True  # Start by expecting a subheader

    for line in lines:
        # Check for subheader
        if expecting_subheader:
            if line.strip():  # If the line is not empty
                subheaders.append(line.strip())
                expecting_subheader = False  # Next, we expect text
                if current_text:  # If there's accumulated text, start a new one
                    texts.append(current_text)
                    current_text = ""
            continue

        # If we're not expecting a subheader, check if we're at the end of a text section
        if line.strip() == "" and not expecting_subheader:  # Check for an empty line indicating end of a text
            expecting_subheader = True  # Next, expect a subheader
        else:
            current_text += line + "\n"  # Add line to current text

    # After the loop, add the last text section if it exists
    if current_text.strip():
        texts.append(current_text.strip())

    return subheaders, texts

# Your text goes here
subheaders, texts = process_text()
print(subheaders)

images = ["images/PIML/initial.webp","images/PIML/piml.png","images/PIML/ew.png"]

def get_images(images = images):
    return images
