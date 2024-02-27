
text = """Introduction to Image Generation
Imagine you're a magician who can create lifelike images from thin air. In the digital world, this magic is performed by algorithms called generative models. These models, like artists, learn from existing images to create new ones, ranging from realistic to fantastical, just based on descriptions.

Generative Adversarial Networks (GANs)
Before our main act, diffusion models, there was a popular duo in town called GANs. Think of GANs as a pair of artists: one creates paintings (the generator), and the other critiques them (the discriminator). The creator strives to make art so convincing that the critic can't tell it's fake. The critic strives to make inspections so precise, that he can't be tricked. This rivalry leads to astonishingly realistic images, but sometimes, the creator gets stuck, making the same type of art over and over—a problem known as "mode collapse."

Introduction to Diffusion Models
Now, enter the diffusion models, a new star in the image-generation landscape. Unlike the competitive nature of GANs, diffusion models work like sculptors, starting with a block of marble (a noisy image) and gradually chiseling away (removing noise) to reveal a masterpiece hidden within.

The Orchestra Analogy
Imagine an orchestra playing with all its instruments, creating a total noise. Our goal is to hear a clear voice or message in this chaos. The diffusion model does this by "listening" to the orchestra and then trying to predict and cancel out some instruments (noise) bit by bit. With each attempt, it gets better at isolating the voice (the image we want to generate) from the cacophony, until finally, the message becomes clear. This iterative process of prediction and cancellation mirrors how diffusion models iteratively remove noise to reveal the desired image.

Training the Model
During its training, the model sees many pictures at different stages of being covered by noise. Instead of guessing the original picture directly from the noisy version, it learns to guess the noise itself. By doing this, it becomes an expert at reversing the noise, step by step, to uncover the image underneath.

Generating New Images
To create a new image, we start with random noise—like the orchestra before it begins playing. Then, we use our model to gradually remove this noise, revealing an image as if finding a clear melody in the music. This process can be influenced by giving the model a hint (like text descriptions) about what image we want to see.

Conditional Image Generation and Classifier-Free Guidance
We can tell our model, "I want a picture of a sunset over the ocean," and it uses this instruction to shape the final image. Classifier-free guidance is like giving the model a more specific hint (e.g., "with vivid colors") to make sure the final image is even closer to what we're imagining.

Practical Applications and Accessibility
Though creating these models requires a lot of computing power, there are versions like Stable Diffusion that let us experiment with generating images without needing a supercomputer. This means anyone can create beautiful, complex images from simple text descriptions, bringing the power of AI-driven creativity to our fingertips.

Conclusion
Diffusion models have transformed the landscape of image generation by offering a stable, flexible approach to creating images from text. By iteratively refining noise into coherent images, they open up endless possibilities for creativity, from art and design to new forms of storytelling. With tools like Stable Diffusion, this magic is now accessible to everyone, not just AI wizards.
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

images = ["images\StableDiffusion\donut.webp","images\StableDiffusion\gan.webp","images\StableDiffusion\sculptor.webp","images\StableDiffusion\orchestra.webp","images\StableDiffusion\paper.JPG",
          "images\StableDiffusion\diffusion.png","images\StableDiffusion\sunset.webp","Nothing","Nothing"]

def get_images(images = images):
    return images