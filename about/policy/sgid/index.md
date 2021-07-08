---
title: SGID Database Policies
author:
  display_name: UGRC Office
  email: ugrc@utah.gov
tags:
  - policy
  - sgid
categories: []
date: 2019-12-04 10:01:27 -0500
---

The following policies apply to data in the internal SGID geodatabase, which is a curated database of state-wide datasets. It is maintained as an internal, UGRC-only Esri Enterprise Geodatabase and is available to everyone as the [Open SGID]({% link sgid/open-sgid/index.md %}) and as part of our [Open Data](https://opendata.gis.utah.gov) site.

1. TOC list
{:toc}

## Adding New Datasets to the SGID Geodatabase
{: .text-left }

We strive to achieve and maintain a high standard of quality for the SGID. We use the following policies and procedures to guide this effort.

### Qualifying Datasets
{: .text-left }

Datasets should meet all the following criteria:

- The dataset should cover a **state-wide** geographic extent, be part of a state-wide project or initiative (such as roads, address points, and parcels), or be relevant to broader projects or mandates that have a state-wide interest (e.g. geologic hazard mapping or endangered species mapping).
- The dataset should be useful to **multiple agencies or organizations'** daily activities or decision-making. Datasets primarily used internally by a single agency aren't great candidates for the SGID.
- The entity providing the dataset should be the **authoritative** or original source (for example, a county's parcels must come from the County government).
- The entity providing the dataset does not have the internal **capability** to publicly serve the data (such as through an existing ArcGIS Online organization). An entity's data storage costs or server capacity may not be sufficient justification for adding data to the SGID.

Agencies and organizations can still share datasets that don't meet the guidelines above with our [Open Data site](https://opendata.gis.utah.gov/). This is a great way to share data mainly intended for the general public with a wide audience. Please see our [Open Data sharing guidelines]({%link about/policy/open-data/index.md %}) for more information.

We will periodically review the SGID for datasets that no longer meet these criteria. Specifically, we may consider removing datasets that see little to no usage for a prolonged period of time.

### Dataset Introduction Process
{: .text-left }

We will use the [Porter](https://github.com/agrc/porter) project to guide and track the steps needed to add or make breaking changes (remove, schema change, etc.) to products contained in the SGID. A brief overview of these steps is included below.

We will add a corresponding record to the [Data Stewardship spreadsheet](https://docs.google.com/spreadsheets/d/11ASS7LnxgpnD0jN4utzklREgMf1pcvYjcXcIcESHweQ/edit#gid=1). This will contain at a minimum:

- The authoritative access from location
- The table name
- A description
- The data steward
- The steward contact name and email
- A link to the data page on the UGRC website
- A link to the SGID Open Data page

We will create a hosted feature service of the dataset in our ArcGIS Online organization. The ArcGIS Online item for this feature service will reside in the corresponding category folder and group and contain the appropriate tags. If the dataset is authoritative, it will be marked as `authoritative`.

The [Auditor](https://github.com/agrc/auditor) project will regularly synchronize the ArcGIS Online item's information (tags, thumbnail, title, metadata, etc.) with information from the SGID geodatabase to ensure consistency across all our platforms.

If the dataset is shared with our [Open Data site](https://opendata.gis.utah.gov/), we will enable the multiple formats download option on the ArcGIS Online item page to allow users to download File Geodatabases and other non-default download options.

We will populate the [minimum metadata content]({% link about/policy/metadata/index.md %}) in the SGID geodatabase. We recommended using the [metadata form](https://docs.google.com/forms/d/1u7gwdmRN-83Kh5zizi-kHRObeoNyaakM3scPkLT3zKY/edit) to create new metadata for the SGID.

The domain values for any new coded value domain must match their corresponding descriptions. Read about this effort in the [improving data clarity with domains](https://docs.google.com/document/d/12bdtmtv-ZVF9g-lFshbobx8DbKX9LfbL44HawLjFTVw/edit?usp=sharing) document.

We will use [Sweeper](https://github.com/agrc/sweeper) (or some other form of automation) to remove all empty or invalid geometries and duplicate records.

The SGID uses the ESRI default Resolution and Tolerance:

- XY Resolution: 0.0001 Meter
- XY Tolerance: 0.001 Meter

### Open SGID
{: .text-left }

All datasets in the SGID geodatabase are synced nightly with the [Open SGID]({% link sgid/open-sgid/index.md %}). This open-standards-centric database is accessible to anyone with an internet connection.

### Dates in Table Names
{: .text-left }

Dates are acceptable in table names when content belongs in either the `census`, `political`, or `tax` categories to identify datasets where the most current data may not reflect the current calendar year. For all other categories, dates should only be used for tables that are no longer effective/active or soon-to-be effective/active. This implies that the **most current and relevant** data contains **no date suffix**. Historical or future data _will_ contain a date suffix to help identification at a glance. The best way to learn about a dataset is to view the data page metadata.

## Updating and Editing Existing Datasets
{: .text-left }

No edits will be made to the internal SGID from 7:00PM to 10:00AM MST to allow for automated scripts to push accurate updates to ArcGIS Online and ArcGIS Server. UGRC will ensure that data is production-ready before the editing window ends.

All database updates will be done during the editing window using [Swapper](https://github.com/agrc/swapper) or some other automated process to reduce the amount of time with incomplete data.

All data updates being pushed into the SGID will have removed empty geometries and duplicate records with [Sweeper](https://github.com/agrc/sweeper) or another automated process.

All edits made to the internal SGID will be captured in the `Last update date` in the metadata, in the [Data Stewardship spreadsheet](https://docs.google.com/spreadsheets/d/11ASS7LnxgpnD0jN4utzklREgMf1pcvYjcXcIcESHweQ/edit#gid=0), and as an update on the UGRC website data page.

If making a schema change, please consider updating any domain descriptions that do not match the domain value. See this [document](https://docs.google.com/document/d/12bdtmtv-ZVF9g-lFshbobx8DbKX9LfbL44HawLjFTVw/edit?usp=sharing) to learn more about this effort.

## Removing Datasets from the SGID Geodatabase
{: .text-left }

Over time, we may remove datasets from the SGID geodatabase for various reasons, some of which include the following:

- We have a new version of the dataset with a substantially different schema.
- The dataset is out-of-date.
- The dataset is no longer being updated by the steward.
- The steward has requested us to remove the dataset.
- A more authoritative source for the dataset exists elsewhere.
- The dataset does not meet the qualifying criteria listed in the "Qualifying Datasets" section above.

Just like when adding data, we will use the [Porter](https://github.com/agrc/porter) project to track and guide dataset deprecation.

We acknowledge the impact removing datasets can have on maps and projects using our datasets. We will do our best to communicate and warn people as quickly as possible through our [@MapUtah](https://twitter.com/maputah) Twitter account and by marking items as `Deprecated` in ArcGIS Online before deleting them. We encourage everyone using our data to follow us on Twitter. The default duration for when deprecation actions are started is 30 days after the first communication. The communication and porter issue will contain migration steps.

### "Static" Datasets
{: .text-left }

We anticipate some SGID datasets won't receive future updates, such as the boundary lines for adjacent counties in the surrounding states. These datasets will be removed from the SGID geodatabase but left in ArcGIS Online, where they will be tagged as `static` and remain members of a Utah SGID group.

### "Shelved" Datasets
{: .text-left }

Over time, we will remove datasets from the SGID geodatabase that are no longer current but continue to have historical value (e.g., Census/ACS data or previous tax district boundaries). Their associated ArcGIS Online items will be tagged as `shelved` and placed in the public [AGRC Shelf](http://utah.maps.arcgis.com/home/group.html?id=8765687b7b0545668fff02d1b750f7a9) ArcGIS Online group for future reference.
