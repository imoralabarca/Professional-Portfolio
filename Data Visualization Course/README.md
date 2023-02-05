# Kickstarter Project



## Getting started

To make it easy for you to get started with GitLab, here's a list of recommended next steps.

Already a pro? Just edit this README.md and make it your own. Want to make it easy? [Use the template at the bottom](#editing-this-readme)!

## Add your files

- [ ] [Create](https://docs.gitlab.com/ee/user/project/repository/web_editor.html#create-a-file) or [upload](https://docs.gitlab.com/ee/user/project/repository/web_editor.html#upload-a-file) files
- [ ] [Add files using the command line](https://docs.gitlab.com/ee/gitlab-basics/add-file.html#add-a-file-using-the-command-line) or push an existing Git repository with the following command:

```
cd existing_repo
git remote add origin https://gitlab.com/imoralabarca/kickstarter-project.git
git branch -M main
git push -uf origin main
```

## Integrate with your tools

- [ ] [Set up project integrations](https://gitlab.com/imoralabarca/kickstarter-project/-/settings/integrations)

## Collaborate with your team

- [ ] [Invite team members and collaborators](https://docs.gitlab.com/ee/user/project/members/)
- [ ] [Create a new merge request](https://docs.gitlab.com/ee/user/project/merge_requests/creating_merge_requests.html)
- [ ] [Automatically close issues from merge requests](https://docs.gitlab.com/ee/user/project/issues/managing_issues.html#closing-issues-automatically)
- [ ] [Enable merge request approvals](https://docs.gitlab.com/ee/user/project/merge_requests/approvals/)
- [ ] [Automatically merge when pipeline succeeds](https://docs.gitlab.com/ee/user/project/merge_requests/merge_when_pipeline_succeeds.html)

## Test and Deploy

Use the built-in continuous integration in GitLab.

- [ ] [Get started with GitLab CI/CD](https://docs.gitlab.com/ee/ci/quick_start/index.html)
- [ ] [Analyze your code for known vulnerabilities with Static Application Security Testing(SAST)](https://docs.gitlab.com/ee/user/application_security/sast/)
- [ ] [Deploy to Kubernetes, Amazon EC2, or Amazon ECS using Auto Deploy](https://docs.gitlab.com/ee/topics/autodevops/requirements.html)
- [ ] [Use pull-based deployments for improved Kubernetes management](https://docs.gitlab.com/ee/user/clusters/agent/)
- [ ] [Set up protected environments](https://docs.gitlab.com/ee/ci/environments/protected_environments.html)

***

# Editing this README

When you're ready to make this README your own, just edit this file and use the handy template below (or feel free to structure it however you want - this is just a starting point!). Thank you to [makeareadme.com](https://www.makeareadme.com/) for this template.

## Suggestions for a good README
Every project is different, so consider which of these sections apply to yours. The sections used in the template are suggestions for most open source projects. Also keep in mind that while a README can be too long and detailed, too long is better than too short. If you think your README is too long, consider utilizing another form of documentation rather than cutting out information.

## Name
Choose a self-explaining name for your project.

## Description
Let people know what your project can do specifically. Provide context and add a link to any reference visitors might be unfamiliar with. A list of Features or a Background subsection can also be added here. If there are alternatives to your project, this is a good place to list differentiating factors.

## Badges
On some READMEs, you may see small images that convey metadata, such as whether or not all the tests are passing for the project. You can use Shields to add some to your README. Many services also have instructions for adding a badge.

## Visuals
Depending on what you are making, it can be a good idea to include screenshots or even a video (you'll frequently see GIFs rather than actual videos). Tools like ttygif can help, but check out Asciinema for a more sophisticated method.

## Installation
Within a particular ecosystem, there may be a common way of installing things, such as using Yarn, NuGet, or Homebrew. However, consider the possibility that whoever is reading your README is a novice and would like more guidance. Listing specific steps helps remove ambiguity and gets people to using your project as quickly as possible. If it only runs in a specific context like a particular programming language version or operating system or has dependencies that have to be installed manually, also add a Requirements subsection.

## Usage
Use examples liberally, and show the expected output if you can. It's helpful to have inline the smallest example of usage that you can demonstrate, while providing links to more sophisticated examples if they are too long to reasonably include in the README.

## Support
Tell people where they can go to for help. It can be any combination of an issue tracker, a chat room, an email address, etc.

## Roadmap
If you have ideas for releases in the future, it is a good idea to list them in the README.

## Contributing
State if you are open to contributions and what your requirements are for accepting them.

For people who want to make changes to your project, it's helpful to have some documentation on how to get started. Perhaps there is a script that they should run or some environment variables that they need to set. Make these steps explicit. These instructions could also be useful to your future self.

You can also document commands to lint the code or run tests. These steps help to ensure high code quality and reduce the likelihood that the changes inadvertently break something. Having instructions for running tests is especially helpful if it requires external setup, such as starting a Selenium server for testing in a browser.

## Authors and acknowledgment
Show your appreciation to those who have contributed to the project.

## License
For open source projects, say how it is licensed.

## Project status
If you have run out of energy or time for your project, put a note at the top of the README saying that development has slowed down or stopped completely. Someone may choose to fork your project or volunteer to step in as a maintainer or owner, allowing your project to keep going. You can also make an explicit request for maintainers.




TO ADD:

The questions that we wanted to explore through our dashboards were: 
- **1.	Dashboard “Terrorism Overview”: Overall, what have been the countries most attacked in both number of attacks and casualties, by year.**
- a.	In the countries/regions of interest of the group (Europe and Venezuela), we wanted to know the development of terrorist attacks across years.
- **2.	Dashboard “Weapons and Target”: How do weapon type changes depending on target type?**
- a.	We added the possibility for the user to select a region or decade of interest, and to display the casualties by weapon type to avoid misleading information (For example, fake weapons are mostly used in airports, but for obvious reasons the casualties are 0)
- **3.	Dashboard “Countries Freedom”: Are free countries less vulnerable than not free countries ?**
- a.	Because instability in the countries depend a lot on the region, we wanted to make this dashboard as interactive as possible so that the user can inspect specifically one country at a time and with the visualizations on the bottom compare across periods where that country was not free or partially free. For example, we found that Venezuela had more terrorist attacks during the period that it was free, and that the main target was the government. On the contrary, while it’s been not free, the main target has been the police. 
- **4.	Dashboard “Terrorist Groups”: Is there a relationship between terrorists’ groups years of activity and total amount of attacks?**
- a.	Depends on each terrorist group. We were able to find out that older groups are not as violent in the same rate as the newer ones. If the newer ones keep up the pace, by the time they reach the same years of activity as the older ones, they will have more attacks accumulated, on average
- **5.	Dashboard “Terrorism Density”: What are the most dangerous countries if we look at terrorist attacks per 1 million citizens?** 
- a.	We were able to see that countries such as El Salvador have the highest rate of terrorist attacks per citizens. This dashboard allows users to select a specific country and find out the most dangerous cities based on that metric

Other remarks:
- 1.	Data cleaning (DataViz_DC.ipynb)
This notebook displays the code used to clean the dataset. Most important issues: only selected fields with less than 2% of null values (confirming this information with TableauPrep). Rows with null values in Days were filled by the mean. Categorical variables with -9 or -99 were replaced with “Unknown”. A new column was created, “Casualties”, to add Wounded and Killed.
- 2.	External data (Adding_data.ipynb)
This notebook was used to add external data, such as GDP, population and the Freedom House Index of each country, by year. We added an identifier, “Country_year”, as key to add the external data. 
- 3.	Tableau
a.	Unknown countries and cities
i.	We changed the name of unknown, currently nonexistent countries, to those that are currently located were these countries were.
ii.	There were around 30k cities that still remained unknown, so we decided to use instead the Latitude and Longitude given by the dataset, which mostly corrected the issue, leaving only around 2k null values.
b.	Several calculated fields were created to help us achieve the desired results, such as:
i.	Casualties by attack, % of count(eventid), Terrorism density, Years Active, and other LOD expressions.


