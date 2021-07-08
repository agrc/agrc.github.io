---
layout: page_nocrumb
tags:
  - sharing
author:
  display_name: AGRC Office
  email: agrc@utah.gov
date: 2017-01-26 23:40:06
title: Sharing GIS Data
categories: []
---

Statewide GIS datasets play a critical role in many personal, commercial, and government projects. We work with cities, counties, and state agencies to ensure that the products available through the [SGID]({% link sgid/index.html%}) provide clean and consistent authoritative data across every geography in the state. This collaborative work has lead to the SGID becoming one of the premier GIS databases in the country. Our webpages have had over 30,000 views and 5,000 downloads, and the (what database?) gets over 15,000 table views a month.

This would not be possible without the help and collaboration of governments and agencies across the state. Many of our most popular datasets—roads, parcels, address points—are all conglomerated from cities and counties, who send us updated data on a regular basis. We then merge them into unified, state-wide datasets available to anyone, free of charge.

Many state agencies have taken advantage of the SGID's broad audience to share important data, too. Many individuals, business, and municipalities use natural hazard layers from the Utah Geological Survey and land ownership boundaries from the Public Lands Policy Coordination Office for site selection and analysis.

We don't just take data—we like to give, too! Under direction of the Lieutenant Governor, we map all the changes to city boundaries from annexations, incorporations, and disconnections to create a statewide municipal boundary dataset. We also coordinate between various state and federal agencies to collect Lidar data for as much of the state as possible. Finally, with the support of the state legislature and cities and counties across the state, we spearhead acquiring state-wide high-resolution aerial imagery.

## Join the party!

We hope you'll join us in our goal to make as much GIS data as possible available to the broadest audience we can. We've put together a [standard process]({% link sharing/process/index.md %}) to make sure your datasets get where they need to go.

#### SGID Index

It all starts with the SGID Index, which aims to be a database of all statewide GIS resources. If you are hosting resources on your own server, we can add links to your datasets to the Index and to the category pages on our website. These pages group similar data together by topic to help people discover relevant datasets.


#### Open Data

We are leveraging Esri's Open Data offering to create [opendata.gis.utah.gov](https://opendata.gis.utah.gov), a central list of ArcGIS Online and ArcGIS Enterprise Portal services. This is a great way to leverage your existing ArcGIS Online or Enterprise infrastructure to share your data with little additional work. We are happy to include any datasets in our Open Data site that meet our [Open Data policies]({% link about/policy/open-data/index.md %}).

#### Open SGID and AGRC's ArcGIS Online Organization

Do you have a statewide dataset but don't have the ability to host or share it yourself? If it meets our [criteria]({% link about/policy/sgid/index.md %}), we will host it in our [Open SGID]({% link sgid/open-sgid/index.md %}) database and share it as a feature service through our ArcGIS Online [organization](https://utah.maps.arcgis.com). The Open SGID is built on open source database technology (Postgres) and is available to anyone with an internet connection via a wide variety of software.

#### ArcGIS Online and Open Data

{% capture contact %}{% include contact.html subject=page.title contact=site.data.contacts.sgid text="Please reach out to " %}{% endcapture %}

If you have an ArcGIS Online account, we can share authoritative data through our [SGID Open Data](https://opendata.gis.utah.gov) and AGRC website. We put together some  to help you share effectively to a larger audience. {{ contact }} to start sharing today!

#### AGRC Website and SGID Index

We are very flexible and skilled at building statewide datasets from disparate sources. We can create a data page on the AGRC website from data shared with us from web services (`https://`, `ftp://`, etc), database connections, website solutions like [Dropbox](https://www.dropbox.com/) or [ShareFile](https://www.sharefile.com/), or something as simple as an [email attachment]({% link about/contact/index.html %}).

We can link to existing services from our [SGID Index]({% link data/sgid-index/index.html %}) if an entire data page is not appropriate. It is very simple and we hope you take advantage of this great partnership opportunity.

#### SGID Database

{% capture contact %}{% include contact.html subject=page.title contact=site.data.contacts.agrc text="If you work on any of these datasets please get in touch with " hide-punctuation=true %}{% endcapture %}

The SGID database is the source of truth for GIS data in Utah. It stores all of the [most important and vital](https://docs.google.com/spreadsheets/d/1FNCvSQxgQbFG--k3ZapscsTapbrxtSGlKqMcMLCsTYs/edit#gid=0) GIS data. SGID Open Data and mapserv all get their data from this source. Listed below are the core layers we strive to keep current through partnerships with county and local government. {{contact}} so we can help improve Utah GIS data.

### Primary Core Datasets
{: .text-left }

- [Road Centerlines]({% link sharing/core-data/index.md %}#road_centerlines)
- [Address Points]({% link sharing/core-data/index.md %}#address_points)
- [Parcels]({% link sharing/core-data/index.md %}#parcels)
{: .dotless }

### Secondary Core Datasets
{: .text-left}

- [Boundaries]({% link sharing/core-data/index.md %}#boundaries)
- [Building Footprints]({% link sharing/core-data/index.md %}#building_footprints)
- [Trails]({% link sharing/core-data/index.md %}#trails)
{: .dotless}

Please read about the [desired schema and attribute information]({% link sharing/core-data/index.md %}) we would like to provide with these data.