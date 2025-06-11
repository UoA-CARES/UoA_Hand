# UoA\_IsaacLab\_Toolkits

Welcome to the **UoA\_IsaacLab\_Toolkits** repository. This project provides a collection of tools and utilities designed to enhance and streamline development within NVIDIA's Isaac Lab, with a special focus on integration with the `skrl` reinforcement learning library.

This toolkit is developed by the University of Auckland to support advanced robotics research, particularly in areas of robot learning, simulation, and real-world deployment.

The core functionalities of our toolkit include:

  * **MuJoCo to Isaac Lab Transfer**: Utilities to convert robot models from MuJoCo's MJCF format to the USD format required by Isaac Sim, simplifying the process of importing existing robots into the Isaac Lab environment.
  * **LLM-based Reward and Environment Generation**: Innovative tools that leverage Large Language Models (LLMs) to automatically generate reward function code and entire environment setups from plain text descriptions, accelerating the RL development cycle.
  * **SKRL Algorithm Customization**: A set of modified algorithms and helper classes to facilitate the customization and extension of the `skrl` library's agents within Isaac Lab.
  * **Real-to-Sim and Sim-to-Real**: Robust pipelines for migrating models and algorithms to physical robots, including support for fine-tuning during the transfer process.

## 1\. Installation

### Prerequisites

Before installing this toolkit, you must have a working installation of **NVIDIA Isaac Lab**. Please follow the official installation instructions carefully.

  * **Isaac Lab Installation**: We recommend the `pip` installation method. For detailed instructions, please refer to the [official Isaac Lab installation guide](https://www.google.com/search?q=https://isaac-sim.github.io/IsaacLab/docs/source/setup/installation/pip_installation.html).

### Toolkit Installation

1.  **Clone the Repository**:
    Clone this repository to your local machine. This repository includes the official Isaac Lab repository as a submodule.

    ```bash
    git clone --recursive https://github.com/your-username/UoA_IsaacLab_Toolkits.git
    cd UoA_IsaacLab_Toolkits
    ```

2.  **Install Isaac Lab**:
    Navigate into the `isaaclab` directory and run the setup script. This will install Isaac Lab and all its required dependencies.

    ```bash
    cd isaaclab
    ./isaaclab.sh -i
    ```

    *Note: This process may take a significant amount of time.*

3.  **Install Toolkit Dependencies**:
    The custom toolkits in this repository may have additional dependencies. Install them using the provided `requirements.txt` file.

    ```bash
    cd ..  # Return to the root of UoA_IsaacLab_Toolkits
    pip install -r requirements.txt
    ```

    *(You will need to create a `requirements.txt` file listing any extra libraries your toolkits use, such as `openai`, `langchain`, etc.)*

## 2\. Structure of the Codebase

This repository is organized to keep the custom toolkits separate from the core Isaac Lab framework, ensuring clarity and maintainability.

```
UoA_IsaacLab_Toolkits/
│
├── isaaclab/                     # The official Isaac Lab repository as a subfolder/submodule.
│   ├── docs/
│   ├── source/
│   └── ...
│
├── mujoco_transfer/              # Scripts for converting MJCF files to USD.
├── llm_reward_generator/         # Tools for generating reward functions from text prompts.
├── llm_env_generator/            # Tools for generating environment code from text prompts.
├── skrl_mods/                    # Customizations and modifications for SKRL algorithms.
├── real_world/                   # Pipelines and tools for Sim-to-Real transfer.
│
├── docs/                         # Documentation specific to this toolkit.
│
├── .gitignore
└── README.md
```

  * **`isaaclab/`**: Contains the unmodified Isaac Lab source code. For any issues or questions related to the core framework, please consult the [official Isaac Lab documentation](https://www.google.com/search?q=https://isaac-sim.github.io/IsaacLab/docs/index.html).
  * **`mujoco_transfer/`**, **`llm_reward_generator/`**, **`llm_env_generator/`**, **`skrl_mods/`**, **`real_world/`**: These directories are the core of our contribution. Each contains a specific tool, complete with its own scripts and potentially its own documentation.

## 3\. How to Use the Toolkits

Below are instructions on how to use the primary features of this toolkit. All commands should be run from the root directory of the repository (`UoA_IsaacLab_Toolkits/`).

### Mujoco to Isaac Lab Transfer

To convert a MuJoCo robot model to a USD asset for Isaac Lab:

1.  Place your `.xml` MJCF file inside the `mujoco_transfer/assets/` directory.
2.  Run the conversion script:
    ```bash
    python mujoco_transfer/convert.py --robot_name <your_robot_name>
    ```
3.  The converted USD file and its configuration will be saved in the `mujoco_transfer/output/` directory, ready to be used in an Isaac Lab environment.

### LLM-based Reward Function Generation

To generate a reward function from a natural language description:

1.  Create a text file (e.g., `my_reward_prompt.txt`) describing the desired reward logic. For example:
    > "Reward the robot for moving its end-effector towards the target. Penalize it for excessive joint movement and for collisions with the ground."
2.  Run the generation script:
    ```bash
    python llm_reward_generator/generate_reward.py --prompt_file <path/to/my_reward_prompt.txt> --output_file <path/to/generated_rewards.py>
    ```
3.  The script will produce a Python file containing a reward class that can be directly imported into your Isaac Lab environment configuration.

### SKRL Algorithm Modification

The `skrl_mods/` directory contains examples of how to modify or extend `skrl` agents. To use a custom agent:

1.  Develop your custom agent logic by inheriting from the base classes provided in `skrl` or our templates.
2.  In your environment's configuration file, update the agent configuration to point to your custom agent class. An example can be found in `isaaclab_tasks` for various robots.

## 4\. Real-to-Sim and Sim-to-Real

A critical component of this toolkit is the support for transferring policies trained in simulation to physical robots. We are actively developing and providing robust pipelines for this process. Our goal is to bridge the "reality gap" by offering tools and methodologies for:

  * **Policy Transfer**: Deploying policies trained in Isaac Lab directly onto real-world hardware.
  * **Fine-Tuning**: Support for on-robot fine-tuning of models to adapt to real-world dynamics and sensor noise.
  * **Data-driven Adaptation**: Collecting real-world data to further improve simulation fidelity and policy robustness.

The `real_world/` directory contains the necessary tools and documentation for these tasks.

## 5\. License

The code specific to **UoA\_IsaacLab\_Toolkits** is licensed under the **[Your License Here, e.g., MIT License]**.

The underlying **NVIDIA Isaac Lab** framework and its dependencies are covered by their own licenses. The Isaac Lab license can be found in the `isaaclab/docs/source/refs/license.rst` file. It is your responsibility to ensure compliance with all applicable licenses.

## 6\. Acknowledgments

  * We extend our gratitude to **NVIDIA** for developing and open-sourcing Isaac Lab, which provides a powerful platform for robotics simulation and research.
  * This work heavily relies on the **skrl library**, and we thank its contributors for creating such a versatile and easy-to-use reinforcement learning library.
  * This project is supported by the **University of Auckland**.