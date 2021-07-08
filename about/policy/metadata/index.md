---
author:
  display_name: UGRC Office
  email: ugrc@utah.gov
tags:
  - metadata
  - sgid
date: 2020-07-09 09:33:34 -0600
title: Basic Metadata Requirements
categories: []
---



Let's take a closer look at the basic elements of SGID metadata. We like to think of these as our minimum requirements.

### Basic SGID Metadata
{: .text-left}

#### Title
{: .text-left}

The title should match the dataset name. If it's a statewide dataset, the title should begin with the word "Utah".

`example: Utah County Boundaries`

#### Tags
{: .text-left}

Tags are included in data searches, so at minimum, each SGID dataset should include the stewarding agency (ie: UGRC), SGID, and the appropriate ISO category tag. We also recommend adding any additional, relevant tags that might help with data discoverability. However, there is no need to include words that are contained in the layer's title (these will be omitted).

All words in tags should be title-cased except for articles (“of”, “the”, “and”, etc.) or abbreviations. Each tag should be separated by a comma. Please refer to [Using tags effectively](https://www.esri.com/arcgis-blog/products/arcgis-online/data-management/using-tags-effectively/) for more ideas and information.

`example: UGRC, SGID, Recreation, Paths, Biking, Hiking, Horseback Riding`

#### Summary
{: .text-left}

The summary should summarize the description in approximately 2 to 3 sentences.

The summary should address the questions presented above in the [summarize your data](#summarize-your-data) section.

#### Description
{: .text-left}

The Description is a more in-depth version of the summary and it should stand on its own. The description should expand on the summary. This is important, particularly, in the event that the summary is missing in the metadata (which is currently the case with [Open Data](https://opendata.gis.utah.gov/) datasets).

The first line of the description should be a date, indicating the last update.

This section should also contain a link to the corresponding [gis.utah.gov data page]({% link data/index.html %})

Additionally, the description should address the questions presented above in the [describe your data](#describe-your-data) section.

#### Credits (as in the source of the data)
{: .text-left}

This should cover who created the dataset and how you can get in contact with them.

The credits should address the questions presented above in the [establish contact info](#establish-contact-info) section.

#### Use Limitations
{: .text-left}

This section covers limitation and licensing on the data.

The language presented here is for reference only and is populated automatically via our [Sweeper](https://github.com/agrc/sweeper) project.

>The data herein, including but not limited to geographic data, tabular data, analytical data, electronic data structures or files, are provided "as is" without warranty of any kind, either expressed or implied, or statutory, including, but not limited to, the implied warranties or merchantability and fitness for a particular purpose. The entire risk as to the quality and performance of the data is assumed by the user.
>[![Creative Commons License](https://i.creativecommons.org/l/by/4.0/88x31.png)](http://creativecommons.org/licenses/by/4.0/){: loading="lazy" }
This work is licensed under a [Creative Commons Attribution 4.0 International License](http://creativecommons.org/licenses/by/4.0/).
