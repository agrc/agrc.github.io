---
title: 'SGID Product Relaunch Update'
author:
  display_name: UGRC Office
  email: ugrc@utah.gov
date: 2019-11-12 18:01:51
categories:
  - Featured
  - Developer
  - SGID Blog
tags: [
  sgid
]
---

In a June 2019 post “SGID Then and Now,” we touched on [where we thought the SGID is going]({% link _posts/2019-06-11-sgid-then-and-now.md %}#where-is-the-sgid-going). Based on the survey responses from that article, we have changed direction in some areas and taken on new tasks in other directions. Now we'd like to share our vision, based on user input, for improving the SGID in general and relaunching the SGID product.

## Redesigned SGID Open Data Website
{: .text-left}

Today we are releasing the redesign of our [SGID Open Data](https://opendata.gis.utah.gov/) website. We think the simple interface of the redesigned website and the new icon set will improve the user experience of searching, browsing, and exploring SGID data! We also updated the [UGRC website]({% link data/index.html %}) icons to make the data navigation experience familiar between the two websites. Esri is working on enhancing the Open Data product, and we are following suit by putting a lot more effort into SGID Open Data into the future. The interface and icon set enhancements mark the beginning.

## Open Data into the Future
{: .text-left}

Over the next few months, the download links on the UGRC website will be transitioning from static Google downloads to Open Data links. This will coincide with the authoritative data being shared through SGID Open Data. This adds new export formats (e.g., file geodatabase, shapefile, KML, and spreadsheet downloads), as well as feature service and GeoJSON APIs. The [UGRC website]({% link index.html %}) will continue to remain the [SGID data index]({% link data/sgid-index/index.html %}) where users can search and learn about SGID data, including data usage, descriptions, update cycles, and downloads for non Open Data content types.

## Static SGID Data Layers
{: .text-left}

Another part of improving the SGID is assessing what information is still relevant to users and making sure that information is current. To surface the best data, we have [trimmed down](https://docs.google.com/spreadsheets/d/1FNCvSQxgQbFG--k3ZapscsTapbrxtSGlKqMcMLCsTYs/edit#gid=0) the number of tables that will reside in the SGID from over 500 to 320. The trimmed layers (i.e., data with historical relevance that are not the most current) are being placed in a [special area](https://utah.maps.arcgis.com/home/search.html?t=content&q=tags%3A%22shelved%22) in ArcGIS Online. These items can still be accessed using the `shelved` tag (e.g., `tags:"shelved"`) but will not receive updates unless there is a specific business case. The convention is to store the most current data in the SGID with no date suffix and tag all prior vintages `shelved` with a year suffix (e.g., TemporalData would reside in the SGID while you would find TemporalData_1990 in ArcGIS Online). We think this organization will help separate the signal from the noise and provide users with the best search experience when using the SGID.

## ArcGIS Online Cleanup
{: .text-left}

We have been using ArcGIS Online for organizations since its inception nearly a decade ago. A lot has changed and improved since then and our past efforts to make the most of this service have created some issues. To remedy those issues, we have correlated a list of all public layers owned by UtahAGRC with their usage stats to identify duplicate and ancillary data. We will be removing the lesser-used duplicates and nonauthoritative data. We hope to avoid disrupting web maps and items that use our data, but we need to tidy up to provide the best experience to our users.

## New Data Editing Policy
{: .text-left}

UGRC continues to improve the way we serve our users. We are currently formalizing our policies on editing data in the SGID database in response to feedback from our users. All active editing will now be performed in an internal SGID database, and edits will be pushed to the public SGID database during off-hours. This will help reduce the risk of interrupting users while they are analyzing data within the time frame stated in our policy[^policy-link]. These new data editing policies mark the maturation of the SGID as a database product and our commitment to treat the SGID as a production service.

### Sweeper Project
{: .text-left}

Along with formalizing our data editing policy, UGRC has started the [sweeper](https://github.com/agrc/sweeper) project to show our commitment to continually increase and stabilize the quality of SGID data. This open-source project gives us constant feedback about an increasing number of data quality metrics. All of the data being loaded into the internal SGID has passed every sweeper check, so all data entering the SGID will be issue free, and the checks are scheduled to run periodically to maintain this high quality of data.

### SGID Data Life Cycle
{: .text-left}

At some point, datasets and applications reach the end of their usefulness. In an effort to stay focused on what is most productive, we occasionally deprecate products. We do our very best to notify our users via [social media](https://twitter.com/MapUtah) and our [newsletter]({% link _posts/2012-11-19-introducing-the-new-agrc-newsletter.md %}) of these deprecations. The deprecations are tracked in an appropriately named repository, [porter](https://github.com/agrc/porter). In this repository, we track all of the dependencies and areas the product touches. We then triage these items to successfully deprecate the product. Please subscribe to updates for that repository, or at the very least subscribe to our newsletter to be informed about possible deprecations. Also, feel free to comment on deprecation issues if you will be affected by them.

## Potential Google Cloud Managed PostGIS
{: .text-left}

UGRC is currently exploring the possibility of expanding the public database to users outside of the State Network with a Google Cloud managed PostGIS database. We are excited for this service since PostGIS can support the open-source GIS community and Esri clients[^esri-requirements]. If this is something that is of interest to you, {% include contact.html subject="PostGIS Beta Opportunity" text="please send an email to " contact=site.data.contacts.webapi hide-punctuation=true %} for a beta testing opportunity. These tests will help determine the feasibility of this solution.

## Open Data Sharing
{: .text-left}

One of our main goals for the SGID moving forward is to continue to cultivate a sense of open data sharing in the Utah GIS community. The SGID Open Data website is a great example of the success of our [data sharing workflow]({% link sharing/process/index.md %}), as you can see from the [authoritative data](https://opendata.gis.utah.gov/search?source=utah%20dnr%20online%20maps%2Cutah%20division%20of%20water%20resources) being shared from our agency partners (DNR Water Resources, DNR Water Rights, and Utah Division of State History). We invite our readers to join these partners and participate in this data-sharing initiative. {% include contact.html subject=page.title text="Please get in touch with " contact=site.data.contacts.sgid %} if you have authoritative ArcGIS Online data to share to the SGID Open Data website.

We are excited for the future of the SGID, and we hope you will get involved to help us provide the highest quality GIS data to the State of Utah.

[^policy-link]: We are working to publish a public copy. This post will be updated when it is available.
[^esri-requirements]: [ArcGIS PostGIS Requirements](https://pro.arcgis.com/en/pro-app/help/data/geodatabases/manage-postgresql/database-requirements-postgresql.htm)
