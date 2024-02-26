
text = """Understanding the Golden Ratio
The Golden Ratio is an irrational number, meaning it cannot be expressed as a simple fraction of two integers. It is defined such that the ratio of the sum of two quantities to the larger one is the same as the ratio of the larger one to the smaller. This property creates the famous "Golden Rectangle," which is believed by some to be the most aesthetically pleasing rectangle shape.

The Fibonacci Connection
The Golden Ratio is closely related to the Fibonacci sequence, a series of numbers where each number is the sum of the two preceding ones. As the sequence progresses, the ratio of successive Fibonacci numbers approximates the Golden Ratio more closely. This relationship has contributed to the mystique surrounding Phi, suggesting a deep connection between mathematics and natural patterns. The fascinating link between the Golden Ratio, eigenvectors, eigenvalues, and the Fibonacci sequence highlights the deep connections in mathematics. Using a simple 2x2 matrix related to the Fibonacci sequence on any two numbers shows how linear algebra can uncover patterns, as the ratio between these numbers tends to align with the Golden Ratio. This pattern, where growth direction matches the matrix's eigenvector, isn't just for Fibonacci numbers; start with any two positive numbers, and through repeated application of this matrix transformation, their ratio will also gravitate towards the Golden Ratio. The location of the vector in the vector space will also gravitate towards the eigenvector of this transformation matrix.

Debunking Myths
Despite its genuine mathematical interest, many claims about the Golden Ratio's prevalence in nature and human creations are exaggerated or false. For example, while it is often stated that the human body, the Parthenon, and the Great Pyramid of Giza are proportioned according to the Golden Ratio, these claims do not hold up under scrutiny. Measurements can be manipulated to find the Golden Ratio where it does not actually exist, and many alleged examples of Phi in nature are based on selective or inaccurate observations.

Golden Ratio in Finance:
The claim that the Fibonacci sequence and the Golden Ratio play a significant role in predicting market movements has garnered attention among traders and analysts. Proponents argue that these mathematical concepts can identify potential levels of support and resistance in price charts, suggesting that natural patterns influence financial markets. However, the validity of this claim is highly debated. Critics argue that while the human brain is adept at recognizing patterns, the tendency to find meaningful correlations in market movements with the Fibonacci sequence or the Golden Ratio may be a manifestation of this pattern-seeking behavior rather than evidence of a reliable predictive tool. Given the vast number of variables influencing market dynamics and the sheer volume of data, it's likely that some market movements will coincidentally align with these ratios. This coincidence does not necessarily imply causation or a deep, underlying mathematical principle governing market behavior. The effectiveness of using the Fibonacci sequence and the Golden Ratio in trading remains a subject of speculation, with success possibly attributed more to chance or self-fulfilling prophecy than to any inherent market law.

True Instances in Nature
However, the Golden Ratio does naturally occur in some instances, particularly in the arrangement of plant leaves, seeds, and flowers. For example, the spirals in pinecones, sunflowers, and pineapples often follow Fibonacci numbers, which are related to the Golden Ratio. This phenomenon is linked to the efficiency of growth patterns, allowing plants to maximize exposure to sunlight and other resources.

Golden Ratio For Survival
The arrangement of leaves or seeds in plants, following the Golden Angle (approximately 137.5 degrees), ensures that each leaf or seed has the optimal space to grow without shading others. This pattern results from the irrational nature of the Golden Ratio, preventing overlaps and ensuring maximum coverage or seed distribution.

Conclusion
The Golden Ratio is a fascinating mathematical constant with real applications and occurrences in nature, particularly in the growth patterns of plants. However, its significance has been overstated in many cases, leading to myths about its universal presence in art, architecture, and the human body. While the Golden Ratio does exemplify the beauty of mathematics and its connections to the natural world, it is important to distinguish between myth and reality, recognizing the true instances of Phi in nature without attributing to it an undue mystical status.

"""

def process_text(input_text=text):
    lines = input_text.split('\n')
    subheaders = []
    texts = []
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

images = ["images/Golden/Grectangle.JPG","images/Golden/eigen.JPG","images/Golden/Dtrump.jpeg","images/Golden/Gtrading.jpg","images/Golden/Gflower.webp","images/Golden/illustration.webp","Nothing"]


def get_images(images = images):
    return images
