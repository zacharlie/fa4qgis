# fa4qgis

Cherry-pick and process a subset of Font Awesome Icons for use as map symbols in QGIS.

Master list stored in the *elements* file.

## Usage

Copy the *svgs* directory from the [Font Awesome Repo](https://github.com/FortAwesome/Font-Awesome/tree/master/svgs) into the project root.

Run the generate python file to extract the "cherry picked" elements.

```~/fa4qgis$ python3 generate.py```

Items to include are stored in the *config.json*.

*checklist.py* is used to sort all available items from the font-awesome style subdirectories by using the global *elements* list.

Run the parameterise script to add QGIS parameters like fill and stroke ```~/fa4qgis$ python3 parameterise.py```.

## Contributing

To review the available icons check the [Font Awesome Gallery](https://fontawesome.com/icons?d=gallery).

In order to improve usability, the following rules should be observed when contributing:

* Keep the core icon set to a minimum functional set. At it's largest, this repo is not expected to grow to more than 200 icons in total (based on the Font Awesome 5 icon series. A "regular" icon and an "outline" icon of the same symbol count as 2 distinct icons).
* Only symbols considered for common/ generic cartography purposes should be used. This includes elements expected to be found in common map products such as transport or tourism elements.
* Include only a single rotation (rotation settings can be manipulated in GIS software). The preferred orientation of included symbols is up, then right, depending on availability e.g. only include angle-up, not angle-up and angle-down etc.
* Icons with additional elements that can be constructed by utilising multiple overlayed symbols, such as strike-through elements etc, should not be included unless the base symbol is not available.
* Elements which have multiple representations should only be represented once (e.g book, book-open, book-reader etc.). An exception to this rule is generic elements which are likely to see multiple uses in various scenarios such as different styles of arrows etc.
* Included icons should endeavour to be neutral and inclusive, not catering to the needs of a specific subset of users based on factors such as culture, race, religion etc (e.g. place of worship).

Additional icons from the font-awesome library may be included by using the [QGIS resource sharing plugin](https://qgis-contribution.github.io/QGIS-ResourceSharing/) be using the repo https://github.com/zacharlie/fa4gis.

This repository will need some sort of governance process going forward. For the time being, the *considerations* is a shortlist of items which should go to a form of poll.

## Licensing

My own code is released under the unlicense. Other components (such as font awesome icons and snippets from other developers) are released under the license conditions stipulated in their relative repositories, such as the The Font Awesome Free License.

## Todo

The config and local download is a quick hack. The reason for JSON as a config file was actually because the intention going forward is to automate this entire process via the GitHub API.
