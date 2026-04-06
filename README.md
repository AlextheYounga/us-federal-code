# US Federal Code on Github
## The Entire US Federal Legal Code in Markdown Format

### DEPRECATED, PLEASE USE LAWSNIPE REPOSITORY
This repo will remain for posterity, but no new updates will be added here.
Instead I will be updating this repo under <a href="https://github.com/Lawsnipe">LawSnipe</a> going forward.

This project aims to make the United States legal code more accessible, transparent, and easier to analyze. By hosting the legal code on GitHub, changes can be tracked in a cleaner manner, enabling greater scrutiny and collaboration.

This repository, compressed stands at 161MB. Expanded into markdown it sits at 681MB.

## Purpose

The primary goals of this repository are:

1. **Public Accessibility**: Provide the US legal code in an easily accessible and readable Markdown format.
2. **Change Tracking**: Use Git's version control to track changes to the legal code, making it clear when and how laws evolve over time.
3. **Scrutiny and Collaboration**: Facilitate public and academic scrutiny of the legal code, enabling meaningful discussions and improvements.
4. **Digestion by LLMs**: Markdown format is easier for Large Language Models (LLMs) to parse, analyze, and learn from, thereby supporting the development of AI tools for legal research and education.

## Repository Structure
- Each section of the US Legal Code is organized into folders and files based on its title and chapter.
- The first document under each folder is called `introduction.md`, which contains introductory information about that particular part, subpart, chapter, or subchapter.
- The lowest level document is a "section", denoted by a "§" symbol.

## Features

- **Readable Format**: Markdown format ensures a clean and readable presentation of the law.
- **Trackable Changes**: Git enables users to view and analyze changes over time.
- **Lightweight**: Pruned non-crucial text minimizes storage requirements while preserving the core content of the law.

## Windows Long Paths Issue
On Windows, you may run into `Filename too long` errors. This is actually not a Windows issue as far as I can tell, but the **git implementation** on Windows. 
The solution is simpler than you might expect.

1. Open "Terminal" in a PowerShell environment. 
2. Run the following command:

```sh
git config --system core.longpaths true
```

This will update the config file located at `C:\Program Files\Git\etc\gitconfig` to add a `core.longpaths = true`.
You should be able to redownload the corpus without issue.

## Contributions
We appreciate your interest in improving this repository! However, I will **not** be accepting pull requests. Instead, we encourage users to open issues to identify areas for improvement. Below are some guidelines:

### Issues

1. **Encouraged Topics**:
   - Suggestions for improving the clarity or accuracy of the Markdown documents.
   - Identification of contradictions or ambiguities within the legal code.
   - Issues related to the specificity of language or missing content.

2. **Civility**:
   - Please keep all discussions civil and constructive.
   - Issues containing disrespectful or inflammatory language will be closed without further consideration.

3. **Substance**:
   - All issues must include a clear description of the problem and a possible improvement or resolution.
   - Issues lacking substance or actionable feedback will be closed.

Thank you for your understanding and cooperation in making this repository as accurate and useful as possible.

## Disclaimer

This repository is not an official source of the US legal code. While every effort has been made to ensure accuracy, users should consult official sources or legal professionals for authoritative information. This project is intended for educational and informational purposes only.


