---
tags:
  - sharing
  - open-data
author:
  display_name: AGRC Office
  email: agrc@utah.gov
date: 2020-01-13 17:00:00
title: Submitting Data to SGID Open Data
categories: []
---

ArcGIS Online items are added to [SGID Open Data]({% link sgid/index.html %}#sgid-open-data-site) by sharing them with one of our SGID groups in ArcGIS Online. This process gives both you and AGRC a chance to review the quality of the item before it is shared. We reserve the right to remove items from these groups if they don't go through this process.

We use [issues](https://guides.github.com/features/issues/) in our [Porter](https://github.com/agrc/porter/issues) repository on GitHub to track a dataset's progress in the submission process and to keep an open and transparent record of everything that happened.

If you've never used GitHub issues before, click here to watch a short tutorial (TBA) about creating an issue.

If you've still got questions after reading this, {% include contact.html subject="SGID Data Additions" contact=site.data.contacts.sgid text='reach out to ' hide-punctuation=true %}, or anyone else on the [AGRC team]({% link about/contact/index.html %}).

### Step 1: 📋 Qualifications (You)
{: .text-left}

First, make sure your dataset meets the SGID qualifications:

- [General qualifications]({% link about/policy/sgid/index.md %}#general-qualifications)
- [SGID Open Data-specific qualifications]({% link about/policy/sgid/index.md %}#sgid-open-data-hub-qualifications)

### Step 2: ✏️ Data Preparation (You)
{: .text-left}

SGID Open Data displays a lot of information from the source ArcGIS Online item:

![An annotated Open Data item]({% link images/od_card_anno.png %}){: .flex .flex--center loading="lazy" }

As noted in the qualifications, make sure the following items are taken care of:

- The ArcGIS Online item is publicly shared
- The item has a good title, description, and tags
- The “Allow others to export data to different formats” in the "Settings" tab is enabled (if possible)
- The "source" value should be set using the method described below

##### Setting the SGID Open Data "Source"

SGID Open Data displays the "source" value on each item and also uses it to sort search results. Thus, it's important for every organization to have a single, unified "source". Esri explains where this value comes from [in this FAQ](https://doc.arcgis.com/en/hub/get-started/frequently-asked-questions.htm#GUID-9843B713-46D2-4938-A961-EC0CD81AE410). Basically, it first searches the ArcGIS Online item's metadata for an organization name. If it doesn't find anything there, it falls back to your ArcGIS organization name.

If you are sharing data from more than one ArcGIS Online user, or you want to customize the name displayed, we suggest setting it in the `Resource > Citation > Contact > Organization Name` metadata field. Otherwise, just leave the metadata contact fields empty and it will use your ArcGIS Online organization name. We use this second way to show "Utah Automated Geographic Reference Center (AGRC)" as the source for all our datasets.

To change the organization name in the ArcGIS Online item's metadata, you need to make sure your ArcGIS Online organization has [metadata enabled](https://doc.arcgis.com/en/arcgis-online/administer/configure-details.htm#ESRI_SECTION1_7FE1F060E03046E692BB36E5F6E3B2AE). Then you can use the Metadata editor on the ArcGIS Online item page to set either field:

![Organization name sources in ArcGIS Online metadata]({% link images/od_agol_md.png %}){: .flex .flex--center .outline loading="lazy" }

The way you upload or overwrite your ArcGIS Online data may also overwrite the item's metadata with info from the source feature class metadata. We suggest you make any changes in both the feature class and ArcGIS Online metadata to avoid problems in the future. In the FGDC CSDGM style, the `Resource > Citation > Contact > Organization Name` field is in `Overview > Citation Contacts`. The `Resource > Contact > Organization Name` field is in `Resource > Points of Contact`.

### Step 3: 💠 Sharing (You)
{: .text-left}

Once your item is prepared, share it with the [SGID Open Data Staging Group](https://utah.maps.arcgis.com/home/group.html?id=3d3bd0d238f24f45b2c4b84f1015a317#overview) (and request access to the group if you're not already a member). This gives us a place to review items before they make it to SGID Open Data.

### Step 4: 📂 Open an Issue (You)
{: .text-left}

Now that all the preparation work is finished, [submit an issue](https://github.com/agrc/porter/issues/new/choose) in Porter using the `Add external data links to the SGID Index` template. Fill out the `Summary` information and check the relevant boxes in the `Submitter's Process` section.

### Step 5: 🔎 Review (You and Us)
{: .text-left}

We will review your submission against the qualifications and reach out with any questions. You can track this in the `AGRC's Process` section of the issue. Once everything looks good, we'll send you an invite to the appropriate SGID group if you're not already a member.

### Step 6: 📤 Publish (You)
{: .text-left}

Once we've worked together to resolve any questions or problems, we'll let you know that the item is ready to be added to SGID Open Data. At this point, you'll need to unshare it from the staging group and share it with the appropriate SGID group.
