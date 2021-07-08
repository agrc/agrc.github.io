---
tags:
  - sharing
  - open-sgid
author:
  display_name: AGRC Office
  email: agrc@utah.gov
date: 2020-01-13 17:00:00
title: Submitting Data to the Open SGID
categories: []
---

If you would like to share data with the [Open SGID]({% link sgid/index.html %}#open-sgid), we will work with you to get a copy of the data. We'll then run checks and reviews on the data to ensure they are clean before being loaded, and we also need to identify when and how we'll incorporate any future updates to the data.

We use [issues](https://guides.github.com/features/issues/) in our [Porter](https://github.com/agrc/porter/issues) repository on GitHub to track a dataset's progress in the submission process and to keep an open and transparent record of everything that happened.

If you've never used GitHub issues before, click here to watch a short tutorial (TBA) about creating an issue.

If you've still got questions after reading this, {% include contact.html subject="SGID Data Additions" contact=site.data.contacts.sgid text='reach out to ' hide-punctuation=true %}, or anyone else on the [AGRC team]({% link about/contact/index.html %}).

### Step 1: 📋 Qualifications (You)
{: .text-left}

First, make sure your dataset meets the SGID qualifications:

- [General qualifications]({% link about/policy/sgid/index.md %}#general-qualifications)
- [Open SGID-specific qualifications]({% link about/policy/sgid/index.md %}#open-sgid-qualifications)

### Step 2: ✏️ Data Preparation (You)
{: .text-left}

Before submitting your data, make sure it's got a stable schema and is ready for public consumption. Make sure the metadata meets our [minimum standards]({% link about/policy/metadata/index.md %}). If you need help with metadata, check out our [basic metadata creation process]({% link sharing/metadata/index.md %}).

Start thinking about the future—how often will this dataset be updated? How will you send those updates to us? Sometimes, outdated data is worse than no data at all. If a user can't find anything, they still know what they don't know. But if they find outdated data without realizing it, they may not know that they are acting on bad data.

### Step 3: 📂 Open an Issue (You)
{: .text-left}

Once you're ready to send your data our way, [submit an issue](https://github.com/agrc/porter/issues/new/choose) in Porter using the `Add data to Open SGID` template. Fill out the `Summary` information and check the relevant boxes in the `Submitter's Process` section.

### Step 4: 💠 Sharing (You)
{: .text-left}

After creating the issue, contact [the AGRC team]({% link about/contact/index.html %}) to work out the best way to share your data with us. We can get the data from you in many different ways:

- We can download it from your choice of cloud storage solutions (Google Drive, Dropbox, etc)
- We can pull it in from an ArcGIS Online/Enterprise Map or Feature Service (our preferred option for frequently-changing data)
- We can set up an FTP share for you to upload it to
- You can just send us a zipped shapefile or GDB via email

### Step 5: 🔎 Review (You and Us)
{: .text-left}

We will review your submission against the qualifications and reach out with any questions. You can track this in the `AGRC's Process` section of the issue.

We run [Sweeper](https://github.com/agrc/sweeper) on all Open SGID datasets to fix empty or duplicate geometries/rows and to double check the metadata. If you'd like, we'll share Sweeper's results with you. Fixing it on your end will help streamline any future data updates, but this isn't necessary to submit the data for the Open SGID. We'll still happily add it to the Open SGID after fixing any issues on our local copy with Sweeper.

### Step 6: 📤 Publish (You and Us)
{: .text-left}

Once we've worked together to resolve any questions or problems, we'll add it to the Open SGID. 

If you sent the data to us as a shpefile or GDB, or as a private or temporary feature service, we will also upload your dataset to our own ArcGIS Online organization as a hosted feature service and share it publicly through Open Data. As part of this process, we will add a thumbnail that includes both the AGRC logo and the relevant SGID category icon to help people searching ArcGIS Online identify SGID data:

![Example ArcGIS Online thumbnail for SGID items]({% link images/agol_location_group.png %}){: .flex .flex--center .outline loading="lazy" }

However, if you maintain maintain your own public feature service of the data, we won't create our own. Instead, please [share your item with SGID Open Data]({% link sharing/open-data/index.md %}).
