import os
import bibtexparser
import collections

### utility function ###

def keep_last_and_only(authors_str):
    """
    This function is dedicated to parse authors, it removes all the "and" but the last and and replace them with ", "
    :param str: string with authors
    :return: string with authors with only one "and"
    """

    last_author = authors_str.split(" and ")[-1]

    without_and = authors_str.replace(" and ", ", ")

    str_ok = without_and.replace(", " + last_author, " and " + last_author)

    return str_ok


def get_bibtex_line(filename, ID):
    start_line_number = 0
    end_line_number = 0

    with open(filename, encoding="utf-8") as myFile:
        for num, line in enumerate(myFile, 1):

            # first we look for the beginning line
            if start_line_number == 0:
                if (ID in line) and not ("@String" in line):
                    start_line_number = num
            else:  # after finding the start_line_number we go there
                # the last line contains "}"

                # we are at the next entry we stop here, end_line_number have the goof value
                if "@" in line:
                    assert end_line_number > 0
                    break

                if "}" in line:
                    end_line_number = num
    assert end_line_number > 0
    return start_line_number, end_line_number


def create_bib_link(ID):
    link = bibtex_filename
    start_bib, end_bib = get_bibtex_line(link, ID)

    # bibtex file is one folder upon markdown files
    #link = "../blob/master/" + link
    link += "#L" + str(start_bib) + "-L" + str(end_bib)

    # L66-L73
    return link


def get_md_entry(DB, entry, add_comments=True):
    """
    Generate a markdown line for a specific entry
    :param entry: entry dictionary
    :return: markdown string
    """
    md_str = ""

    if 'url' in entry.keys():
        md_str += "- [**" + entry['title'] + "**](" + entry['url'] + ") "
    else:
        md_str += "- **" + entry['title'] + "**"

    md_str += ", (" + entry['year'] + ")"

    md_str += " by *" + keep_last_and_only(entry['author']) + "*"

    md_str += " [[bib]](" + create_bib_link(entry['ID']) + ") "

    md_str += '\n'

    if add_comments:
        # maybe there is a comment to write
        if entry['ID'].lower() in DB.strings:
            #print("Com : " + entry['ID'])
            md_str += " \n *"
            md_str += DB.strings[entry['ID'].lower()]
            md_str += "* \n"

    return md_str


def get_md(DB, item, key, add_comments):
    """
    :param DB: list of dictionary with bibtex
    :param item: list of keywords to search in the DB
    :param key: key to use to search in the DB author/ID/year/keyword...
    :return: a md string with all entries corresponding to the item and keyword
    """

    all_str = ""

    #list_entry = {}
    list_entry = collections.OrderedDict()

    number_of_entries = len(DB.entries)
    for i in range(number_of_entries):
        if key in DB.entries[i].keys():
            if any(elem in DB.entries[i][key] for elem in item):
                str_md = get_md_entry(DB, DB.entries[i], add_comments)
                list_entry.update({str_md:DB.entries[i]['year']})


    #sorted_tuple_list = sorted(list_entry.items(), reverse=True, key=lambda x: x[1])
    sorted_tuple_list = list_entry.items()
    for elem in sorted_tuple_list:
        all_str += elem[0]

    return all_str


def get_outline(list_classif, filename):
    str_outline = "# FEP and Active Inference Paper Repository \n"

    str_outline += "This repository provides a list of papers that I believe are interesting and influential on the Free-Energy-Principle, or in Active Inference. If you believe I have missed any papers, please contact me at *beren@millidge.name* or make a pull request with the information about the paper. I will be happy to include it. \n\n"

    str_outline += "## FEP Outline \n"

    str_outline += "This list is of papers focused specifically on the abstract mathematical formulation of the Free-Energy-Principle (FEP). The FEP is a theory which tries to determine the behaviours a non-equilibrium thermodynamical system *must* exhibit if it is to maintain itself as a separate entity over time. It argues that any such system must minimize a quantity called the free energy and that, over the course of this minimisation, behaviour much like action and perception must emerge. \n \n"
    str_outline += "The key prerequisites for the FEP is that a 'system' has a special kind of statistical separation from the world called a Markov Blanket, which it must maintain if it is to remain a system, and that the system possesses a non-equilibrium steady state which it self-organises to and tries to maintain over time against the dissipative forces of entropy. \n \n"
    str_outline += "Much of the work in the FEP has been applying its general tenets to understand biological far-from-equilibrium systems, especially the brain. \n \n"
    str_outline += "If you are just starting out, I reccomend reading all the papers in the 'Survey' section in order. These are all great tutorials or overviews which should give you a great grounding in the intuitions of the theory, and then the later two tutorials should start building up much of the mathematical core of the theory (especially around predictive coding). \n \n"
    for item in list_classif:
        str_outline += "- [" + item[0] + "](https://github.com/BerenMillidge/FEP_Active_Inference_Papers/blob/master/" + filename + "#" \
                       + item[0].replace(" ", "-").lower() + ')\n'

    return str_outline

def get_AIF_outline(list_classif, filename):

    str_outline = " \n \n"

    str_outline += "## Active Inference Outline \n"

    str_outline += "Active Inference is a process theory of neurobiological function inspired by and closely related to the FEP. However Active Inference stands independent of the FEP and can be true even if the FEP is not, and similarly can potentially be falsified without impacting the FEP. The core idea behind Active Inference is the idea that the brain performs both action and perception by variational inference on a unified objective function. \n \n"
    str_outline += "In effect, the key idea behind active inference is that our brains possess powerful probabilistic generative models and inference engines, and that to select actions, we repurpose this powerful capacity we use for perception to also *infer* potential actions. Hence *Active* Inference. \n \n"
    str_outline += "This high-level description leaves open the exact *type* of models and inference being used for action inference in the brain. The active inference literature contains three clear strands of work, which correspond to different assumptions on the exact form of generative models which are proposed to be utilized by the brain. *Discrete* active inference focuses on models of discrete state-spaces parametrised by categorical distributions and transition matrices. *Continuous* active inference focuses on the continuous time case with (generally) linear dynamics, and *Deep* active inference focuses on using deep neural networks to 'scale up' active inference by amortising probabilistic distributions with learned maps. \n"
    str_outline += "The discrete-state-space work has close similarities with bandit-problems and neuroscience tasks and forms a tractable test-bed to understand different kinds of behaviour. Most of the work of creating active inference models of brain function (or dysfunction) lies within this paradigm. Continuous active inference, which is being used for robot control, has close links to classical control theory, while Deep active inference has close links with reinforcement learning and machine learning. \n \n"
    str_outline += "The task of inferring actions (requiring detailed models of future outcomes given these actions), is a subtly more complex task than simply inferring the immediate causes of sensory data as in perceptual inference. It therefore requires different objective functionals (the *expected* free energy) and potentially more advanced message-passing inference algorithms. This work is summarised in the 'Message Passing and Free Energies' section. \n \n"
    str_outline += "\n \n"
    for item in list_classif:
        str_outline += "- [" + item[0] + "](https://github.com/BerenMillidge/FEP_Active_Inference_Papers/blob/master/" + filename + "#" \
                       + item[0].replace(" ", "-").lower() + ')\n'

    return str_outline

def get_acknowledgements():
    str_outline = "\n \n"
    str_outline += "## Acknowledgements \n \n"
    str_outline += "Many thanks to @conorheins for his helpful suggestions. \n \n"
    return str_outline

def get_footnote_string():
    str_outline = "\n \n"
    str_outline += "## Contributing \n \n"
    str_outline += "To contribute, please make pull requests adding entries to the bibtex file.  \n \n The README file was generated from bibtex using the `bibtex_to_md.py` file. \n The keywords to use for each classification (Survey, Discrete-state-space etc) can be found at the bottom of the .py file. \n"
    str_outline += "\n \n"
    str_outline += "*This code and structure is heavily inspired by https://github.com/optimass/continual_learning_papers.*"
    return str_outline


def generate_md_file(DB, list_classif, AIF_list_classif, key, plot_title_fct, filename, add_comments=True):
    """
    :param DB: list of dictionnary with bibtex
    :param list_classif: list with categories we want to put inside md file
    :param key: key allowing to search in the bibtex dictionary author/ID/year/keyword...
    :param plot_title_fct: function to plot category title
    :param filename: name of the markdown file
    :return: nothing
    """

    all_in_one_str = ""
    # FEP section
    all_in_one_str += get_outline(list_classif, filename)

    for item in list_classif:

        str = get_md(DB, item, key, add_comments)

        if str != "":
            all_in_one_str += plot_title_fct(item)
            all_in_one_str += str

    # Active Inference section
    all_in_one_str += get_AIF_outline(AIF_list_classif, filename)
    
    for item in AIF_list_classif:
    
        str = get_md(DB, item, key, add_comments)

        if str != "":
            all_in_one_str += plot_title_fct(item)
            all_in_one_str += str

    all_in_one_str += get_acknowledgements()
    all_in_one_str += get_footnote_string()

    f = open(filename, "w")
    f.write(all_in_one_str)
    f.close()

if __name__ == '__main__':
    bibtex_filename = "bibtex.bib"
    file_name = 'bibtex.bib'
    with open(file_name) as bibtex_file:
        bibtex_str = bibtex_file.read()

    bib_db = bibtexparser.loads(bibtex_str, parser=bibtexparser.bparser.BibTexParser(ignore_nonstandard_types=False))

    ################################### Create Readme ####################################
    def plot_titles(titles):
        return '\n' + "## " + titles[0] + '\n'

    FEP_list_types = [["Surveys", "survey"],
                ["Classics","classic"],
                ["Philosophical Analyses","philosophy"],
                ["Self-Organisation and Markov Blankets","self-organisation"],
                ["Information Geometry","information_geometry"]]
    AIF_list_types =[["Surveys and Tutorials","tutorial"],
                    ["Discrete State Space Formulation","discrete"],
                    ["Continuous Time Formulation","continuous"],
                    ["Message Passing and Free Energies","free_energy"],
                    ["Active Inference for Control Theory/Robotics","robotics"],
                    ["Deep Active Inference", "deep"]]

    generate_md_file(DB=bib_db, list_classif=FEP_list_types,AIF_list_classif=AIF_list_types, key="keywords", plot_title_fct=plot_titles, filename= "README.md", add_comments=True)
