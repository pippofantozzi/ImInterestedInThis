
text = """The Big Idea
NEAT is like nature-inspired problem-solving for artificial intelligence. It's a technique where you let a population of neural networks evolve and adapt over generations to get better at a particular task. Just like how species evolve over time, NEAT evolves neural networks.

Meet the Neural Networks
In NEAT, our "creatures" are neural networks, which are computational models inspired by the human brain. These networks consist of nodes (like neurons) and connections (like synapses). Nodes process information, and connections transmit it.

Innovation through Mutation
To kick off evolution, we introduce some creative chaos. NEAT uses mutation to tweak the neural networks. Think of it like genetic mutations in living beings - some changes happen randomly. In NEAT, mutations can involve adding or removing nodes and adjusting connection weights. These changes bring variety to the population.

Family Matters - Speciation
Now, here's where NEAT gets family-oriented. Instead of having a giant, chaotic pool of mutants, NEAT organizes creatures into species. This is like having different families, each with its own set of characteristics. Speciation ensures that similar creatures stick together.

Survival of the Fittest - Fitness Function
In NEAT, each creature gets a grade on how well it performs the task at hand. We call this the fitness score. Just like in nature, the higher the fitness, the better the chances of survival. Creatures with higher fitness scores get to contribute their traits to the next generation through reproduction.

Evolving Through Generations
Now, let's talk about generations. NEAT works in cycles. Each cycle is a generation, and as creatures reproduce, the population evolves. The magic is in selecting parents with good fitness scores and letting them contribute their traits to the next generation.

Crossover - Mixing Traits
When creatures reproduce, their traits mix. NEAT uses a process called crossover, where the traits of two parents are combined to create a new creature. This is akin to how genes from two parents combine in biological reproduction.

Staying Organized
Remember the species we talked about earlier? Well, NEAT wants to make sure these species don't go extinct. Over time, if a species is struggling, NEAT might allow it to undergo more mutations to see if something useful pops up.

Wrapping Up
In a nutshell, NEAT is like a guided, creative force in the world of AI. It starts with simple neural networks, introduces randomness through mutations, organizes them into families, lets the best performers have babies, mixes traits through crossover, and repeats the process over generations.
This algorithm has a knack for finding innovative solutions to complex problems, all while mimicking the beauty of evolution. So, if you're ever tasked with evolving some AI creatures, NEAT might just be your go-to guide.

Right-sizing the Brain - A Developer's Dilemma
Now, let's tackle a challenge developers often face - figuring out the ideal size and structure of a neural network for a specific task. It's a bit like designing a brain, and it's not always clear how many neurons (nodes) and connections (synapses) are needed.
Traditionally, developers might go for a fully connected network, meaning each node in one layer is connected to every node in the next. It's like having every part of the brain talk to every other part, which can be a bit overkill and computationally expensive.

Enter NEAT - The Architect
NEAT takes a different approach. Instead of developers playing architect and deciding on the network structure, NEAT lets evolution figure it out. It starts with a simple network and allows it to grow in complexity as needed. This is a bit like letting the brain adapt to the task at hand.

Nodes, Not All Created Equal
One brilliant feature of NEAT is recognizing that not all nodes are equally important. In a fully connected network, every node seems crucial, but NEAT introduces the concept of "unimportant" nodes. Some nodes might not contribute much to the task, and NEAT is smart enough to skip connecting them where it's not necessary.

Structured Simplicity
The beauty of NEAT is in its ability to find a balance between simplicity and effectiveness. It's like having a brain that is complex where it needs to be but doesn't waste energy on unnecessary connections. This not only saves computational resources but also makes the whole learning process more efficient.

The Evolutionary Advantage
NEAT's evolutionary approach shines here. Through generations, it fine-tunes the network structure. If a node or connection isn't pulling its weight, evolution might phase it out. On the other hand, if a new node or connection proves useful, it gets to stick around and contribute to the network's success.

Embracing Uncertainty
In the world of AI, tasks can be unpredictable. What works for one might not work for another. NEAT acknowledges this uncertainty and adapts. It's like having a versatile brain that can morph and change its structure based on the challenges it faces.

Conclusion
So, while developers might wrestle with the decision of how big or small a neural network should be, NEAT says, "Let's let evolution decide!" It's a bit like having an AI architect that not only designs but also refines and optimizes the structure based on what works best for the task at hand. NEAT isn't just an algorithm; it's an AI design philosophy that elegantly tackles the challenges of neural network sizing and connectivity.
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

images = ["webimages\evolution.png","webimages\euralnetworks.jpg","webimages\mutations.png","webimages\speciation.jpeg","webimages\survival.webp",
          "webimages\evolution.jpg","webimages\crossover.png","Nothing","Nothing","webimages\deepneuralnet.jpg","webimages\eatstructure.png",
          "Nothing","webimages\oocomplex.gif","webimages\generations.jpg","Nothing","Nothing"]


def get_images(images = images):
    return images