---
tags:
  - sharing
author:
  display_name: AGRC Office
  email: agrc@utah.gov
date: 2020-01-13 17:00:00
title: Submitting Data to the SGID
categories: []
---

Thank you for wanting to share your data with the SGID! We've put together a few processes to make sure your datasets are added to the right place. We use [issues](https://guides.github.com/features/issues/) in our [Porter](https://github.com/agrc/porter/issues) repository on GitHub to track where a dataset is at in the process and keep an open and transparent record of everything that happened.

If you're not sure which part of the SGID you should share your data with, check out our sharing [introduction]({% link sharing/index.md %}#join-the-party) for an overview.

If you've still got questions after reading this, {% include contact.html subject="SGID Data Additions" contact=site.data.contacts.sgid text='reach out to ' hide-punctuation=true %}, or anyone else on the [AGRC team]({% link about/contact/index.html %}).

## Contributing Data to an Existing Dataset

If you have data you'd like to add to an existing dataset, please check the data page for the contact info of the AGRC staffer responsible. If none are listed, please reach out via our main email. We are happy to work with authoritative stewards and other qualified individuals to improve our data.

## Submitting New Datasets

No matter where your datasets fit best—SGID Index, Open Data, or Open SGID—the process begins with the same first two steps: first, making sure your datasets meet the relevant [qualifications]({% link about/policy/sgid/index.md %}) and then opening an issue in [Porter](https://github.com/agrc/porter/issues) using the relevant template.

Each template includes questions about your data. We'd appreciate it if you fill all these out when you first submit your datasets. Otherwise, the issue will be put on hold until this information is provided.

If you're new to all this, please don't hesitate to {% include contact.html subject="SGID Data Additions" contact=site.data.contacts.agrc text='reach out to ' hide-punctuation=true %}. We're happy to help guide you through the process.

### SGID Index
{: .text-left}

It's quite simple to list [qualifying]({% link about/policy/sgid/index.md %}) data in the SGID Index. After you submit an issue in Porter using the `Add data to the SGID Index template`, we will review your submission against the qualifications and reach out with any questions. Once we've worked together to resolve any questions or problems, we'll add your dataset to the SGID Index and close the issue.

### Open Data
{: .text-left}

Adding data to [opendata.gis.utah.gov](https://opendata.gis.utah.gov) requires a few additional steps to navigate the ArcGIS Online sharing mechanics. This time you'll use the `Add data to Open Data` issue template. After the issue is opened, you'll need to request access to the [Open Data Staging Group](https://utah.maps.arcgis.com/home/group.html?id=3d3bd0d238f24f45b2c4b84f1015a317) in ArcGIS Online. This is a staging group that allows us to review the dataset before sharing it through Open Data.

Once we've verified the dataset meets the qualifications, you can share it with the appropriate Utah SGID ArcGIS Online group. All items in these groups are automatically added to Open Data. If this is your first time sharing a data with the particular group, you'll need to request access to the group.

Datasets that languish in the staging group, or that are added to a Utah SGID group without approval, may be removed according to our [policies]({% link about/policy/open-data/index.md %}).

### Open SGID and ArcGIS Online
{: .text-left}

The Open SGID is the latest evolution of the traditional "SGID as a single geospatial database" model. Maintaining data in the Open SGID requires the most work, both on the front end and for long-term maintenance. We encourage you to share your data via Open Data or the SGID Index whenever possible. However, we may pull some datasets into the Open SGID that otherwise belong elsewhere in order to maintain consistency and familiarity with previous versions of the SGID geodatabase. This is done at our discretion according to our [policies]({% link about/policy/open-sgid/index.md %}).

After opening an issue with the `Add data to the Open SGID` template, you'll need to reach out and arrange the best way to transfer your data to us for the first review. We can download data from a cloud storage solution (Google Drive, Dropbox, etc), pull it in from an ArcGIS Online Map or Feature Service, set up an FTP share for you to upload it to, or just have you email us a zipped shapefile or GDB.

Once we get your data, we will run [Sweeper](https://github.com/agrc/sweeper) on it to identify and fix empty and duplicate geometries and rows and to double check the metadata. We'll share the results of this with you as a courtesy—fixing it at the source will help streamline any future data updates, but we'll happily add it to the Open SGID after fixing it on our end with Sweeper.

Nothing is worse than outdated data. If you can't find any data, you know that you may not know what's going on. But, if you find outdated data, you may not know that you are acting on bad data. Consequently, once your dataset has been accepted into the Open SGID, it's important you send any data updates to us. We'll work with you to identify the best way to feed updates into the Open SGID as part of the submission process.

As part of the Open SGID process, we will also upload your dataset to our own ArcGIS Online organization as a hosted feature service and share it publicly through Open Data. We will add a thumbnail that includes both the AGRC logo and the relevant SGID category icon to the ArcGIS Online item to help people searching ArcGIS Online identify SGID data.
