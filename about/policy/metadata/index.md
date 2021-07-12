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

Effective metadata helps people understand the source of a dataset, how up-to-date it is, and any of its inherent restrictions or limitations. Listed below are the minimum metadata items that should be present in any SGID datasets. These correspond to the Esri [Item Description](https://pro.arcgis.com/en/pro-app/latest/help/metadata/view-and-edit-metadata.htm) metadata style and the metadata displayed on an item's ArcGIS Online page.
## Basic SGID Metadata

#### Title
{: .text-left}

The title should match the dataset name. If it's a statewide dataset, the title should begin with the word "Utah".

Example: `Utah County Boundaries`

#### Tags
{: .text-left}

Tags are used by ArcGIS Online in its search algorithms and can be used in Open Data to group data. At a minimum, each SGID dataset's tags should include the stewarding agency (ie: UGRC), "SGID", and the appropriate category name. We also recommend adding any additional, relevant tags that might help with data discoverability. However, there is no need to include words that are contained in the layer's title (these will be omitted).

All words in tags should be title-cased except for articles (“of”, “the”, “and”, etc.) or abbreviations. Each tag should be separated by a comma. Please refer to [Using tags effectively](https://www.esri.com/arcgis-blog/products/arcgis-online/data-management/using-tags-effectively/) for more ideas and information.

Example: `UGRC, SGID, Recreation, Paths, Biking, Hiking, Horseback Riding`

#### Summary
{: .text-left}

The summary should _briefly_ explain the dataset in under 250 characters (an ArcGIS Online limitation). It is primarily used when reviewing ArcGIS Online search results. The summary may end up being very similar to the dataset name for some datasets.

Example: `Utah public library and bookmobile locations`

#### Description
{: .text-left}

The description is a more in-depth version of the summary and should stand on its own. It is a great place for details on the source of the data, how frequently it's updated, its usability at certain scales, or any common misconceptions. A good description is also important because it's the main info displayed in [Open Data](https://opendata.gis.utah.gov/) (the summary is not shown).

The first line of the description should be be the date the dataset was last updated so people have a clear and consistent place to see how fresh or stale it is.

For datasets hosted by UGRC, this section should also contain a link to the corresponding [gis.utah.gov data page]({% link data/index.html %}).

#### Credits (as in the source of the data)
{: .text-left}

The credits should clearly state who created the dataset and how you can get in contact with them.

Example: `UGRC, UDOT`

#### Use Limitations/Terms of Use
{: .text-left}

This section includes both usage limitations (any constraints on where or how the dataset can be used, including disclaimers and attribution rules) and the intellectual property license (if any) associated with the dataset (like Creative Commons).

We use [Sweeper](https://github.com/agrc/sweeper) to automatically populate our hosted datasets with our standard [disclaimer]({% link about/policy/license-disclaimer/index.md %}#disclaimer) and [license]({% link about/policy/license-disclaimer/index.md %}#license).

Open Data will try to find references to the common licenses and will link to the appropriate license. Otherwise, it just lists "Custom License" and displays the item's Terms of Use text.
