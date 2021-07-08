---
layout: page_nocrumb
tags:
  - sharing
author:
  display_name: Michael M. Foulger
  email: michaelfoulger@utah.gov
date: 2019-11-12 13:40:06
title: Sharing Data through the SGID Open Data Site
categories: []
---

![Open Data Homepage]({% link images/od_homepage.png %}){: .flex .flex--center .outline loading="lazy" }

Does your department or division have authoritative datasets hosted in your own ArcGIS Online organization? Do you want to make them easy to find by anyone searching for Utah GIS Data? Share them on the [SGID Open Data website!](https://opendata.gis.utah.gov/) This makes them them easily discoverable while giving you full control over when they are updated.

## Adding Your Data to Open Data

All you need to do is **share your ArcGIS Online items with the appropriate SGID groups**. Items shared with these ArcGIS Online groups are automatically added to the SGID Open Data site.

First, you have to be a member of the SGID groups that are the best fit for your datasets. Reach out to [AGRC staff]({% link about/contact/index.html %}) to request an invite. We'll work with you to identify what datasets are good matches for the SGID Open Data site and what group they best fit in.

Once you're a member of the groups, share each approved item to the appropriate group. You also need to make sure the item is shared with "Everyone (public)". Otherwise, it will only be visible to you (or other members of your organization if shared to the organization) in Open Data.

## Presentation Tips

![An annotated Open Data item]({% link images/od_card_anno.png %}){: .flex .flex--center loading="lazy" }

- The **title** is the first place people look for information. Because items in Open Data are also ArcGIS Online items that are searchable by anyone in the world, we have added "Utah" to the beginning of every title of our public ArcGIS Online items to provide better context.
- A **user name** that includes the department/division's name or function helps users know where the dataset is coming from. For example, all the datasets we share are owned by the `UtahAGRC` user.
- Open Data displays the text from the `Description` field of the source ArcGIS Online item for the **description**. You shouldn't count on any information in the ArcGIS Online `Summary` field to show up unless it's repeated in the description.
- To help with searching, we include the "AGRC" and "SGID" **tags** on all our items while removing any tags that are repeated in the item's title. Please refer to Esri's [post about using tags effectively](https://www.esri.com/arcgis-blog/products/arcgis-online/data-management/using-tags-effectively/) for more ideas and information.
- The "Last Updated" **date** is based on the last time the _ArcGIS Online item_ was changed, not the _data itself_. Things like updating the item's description or changing the thumbnail may update this date. For some frequently-updated datasets, we include the last update date in the description text or refer to the layer's description page on [gis.utah.gov/data]({% link data/index.html %}).
- Keeping your **data schema** constant is a real help to your users. Some will be using your feature services directly in their webmaps rather than self-hosting a copy of your data and trying to keep it up-to-date. Removing fields or changing their types can break popups, search widgets, and other functionality. Adding new fields is less dangerous.
- By default, users can't download spatial datasets from ArcGIS Online/Open Data as **File Geodatabases**. To enable this, go to the item's page in ArcGIS Online and click on the "Settings" tab. Scroll to the bottom and check the box to "Allow others to export data to different formats".
  - NOTE: This will also allow people to export/copy some or all of the features if they add the dataset as a layer in ArcGIS Pro.

## Taming the Sources List

When a user clicks on a data category or searches for a dataset on the SGID Open Data site, a "sources" filter list appears on the search results page. Currently, **it can only show a max of ten sources**. Once we have more than ten in all our Open Data (not just the current search), we don't have any control over which ones are shown. In addition, the free-entry text box above the list requires a perfect text match, so it doesn't help users discover other sources either.

We've tried to be careful with our data to keep any superfluous sources out of this list, and we'd appreciate your help with this as well. Please ensure you've only got one "source" value for your department or division.

So where do the source values come from? Esri explains it [in this FAQ](https://doc.arcgis.com/en/hub/get-started/frequently-asked-questions.htm#GUID-9843B713-46D2-4938-A961-EC0CD81AE410). The main take away is that it first searches the **ArcGIS Online item's metadata** for an organization name. If it doesn't find anything there, it falls back to your **ArcGIS organization name**.

If you'd like to customize the name displayed in the sources list, we suggest setting it in the `Resource > Citation > Contact > Organization Name` metadata field. Otherwise, make sure the metadata contact fields are empty and let it pick up your ArcGIS Online organization name. We use this second way to show "Utah Automated Geographic Reference Center (AGRC)" as the source for all our datasets.

To change the organization name in the ArcGIS Online item's metadata, you need to make sure your ArcGIS Online organization has [metadata enabled](https://doc.arcgis.com/en/arcgis-online/administer/configure-details.htm#ESRI_SECTION1_7FE1F060E03046E692BB36E5F6E3B2AE). Then you can use the Metadata editor on the ArcGIS Online item page to set either field:

![Organization name sources in ArcGIS Online metadata]({% link images/od_agol_md.png %}){: .flex .flex--center .outline loading="lazy" }

Depending on how you upload or overwrite your ArcGIS Online data, it may also overwrite the item's metadata with info from the source **feature class metadata**. We suggest you make any changes in both the feature class and ArcGIS Online metadata to avoid problems in the future. In the FGDC CSDGM style, the `Resource > Citation > Contact > Organization Name` field is in `Overview > Citation Contacts`. The `Resource > Contact > Organization Name` field is in `Resource > Points of Contact`.

## Other ArcGIS Online Considerations

- While they don't appear in the Open Data site, your items' **thumbnails** will appear when a user searches for your data on ArcGIS Online. A [branded thumbnail](https://www.esri.com/arcgis-blog/products/arcgis-online/data-management/put-your-best-thumbnail-forward/) tells users that this is an authoritative dataset. For example, we have use thumbnails that include the category logo for all the SGID data we share.

- Similarly, if you are the original or authoritative source for a dataset, consider setting the **"Authoritative"** checkbox in the ArcGIS Online item's settings. This helps users decide which dataset to use when their search in ArcGIS Online returns several similar results.
