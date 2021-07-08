---
layout: page_nocrumb
tags:
  - sharing
author:
  display_name: Rick Kelson
  email: rkelson@utah.gov
date: 2017-01-26 23:40:06
title: State - Local GIS Data Partnerships
categories: []
---

Statewide GIS map data layers fulfill a critical need for many organizational business needs, including:

| 911 & NextGen 911 (forthcoming) | Blue Stakes (811) Statewide Utility Notification | Utah Department of Transportation| State & Regional Economic Development |
| Complete Count Preparation for 2020 Census | Utah State Tax Commission | Utah Department of Natural Resources | Statewide Elections Management & Redistricting |

UGRC works with partner agencies and local government toward standardization and interoperability of GIS data resources for reliable and consistent information at a statewide level. The State Geographic Information Database provides a 'one-stop-shop' to make discovery, access, and publishing of GIS data efficient.

UGRC has also led partnership efforts to fund, procure, and distribute additional GIS data products, such as aerial photography and lidar purchased through cooperative efforts. Below are are examples of some of those products:

| Aerial Imagery Acquisition (Statewide Hi Res Program) | Aerial Photography Web Services | Custom Base Map Web Services (w/local&state Data) |
| Address Geocoding Web Service | Lidar Acquisition (Statewide 3DEP-Type Program) | Lidar Acquisition (3DEP-type Projects) |
| Realtime GPS Correction Service | Highway Milepost Reference | Highway Exit Numbers and Names |
| State Agency Data Layers in SGID (DNR, DEQ, SITLA) | USGS Topo Quad Web Services | State Cadastral Grant Funding |

GIS data can be shared to AGRC for publication in the State Geographic Information Database (and related web serves) via the [SGID Open Data site]({% link sharing/open-data/index.md %}), [email]({% link about/contact/index.html %}), [Dropbox](https://www.dropbox.com/), [ShareFile](https://www.sharefile.com/), or we can pull from an ArcSDE connection or web-accessible file geodatabase or shapefile (https://, ftp://, etc.).


Listed below are the layers we hope to complete and keep current through partnership with county and local government, and the desired attribute information.

### Primary Datasets
{: .text-left}

- [Road Centerlines](#road_centerlines)
- [Address Points](#address_points)
- [Parcels](#parcels)
{: .dotless }

### Secondary Datasets
{: .text-left}

- [Boundaries](#boundaries)
- [Building Footprints](#building_footprints)
- [Trails](#trails)
{: .dotless}

![GIS Data Samples]({% link images/DataRequest.png %}){: style="width:100%" loading="lazy" }

---
{: .divider }

### [Road Centerlines]({% link data/transportation/roads-system/index.html %} "Road Centerlines page"){: #road_centerlines }

![Road Centerlines]({% link images/90x90_utah-gis-highway-lrs-udot.png %}){: .pull-right .outline loading="lazy" }

This is a multi-purpose statewide roads dataset for cartography and range based-address location. View our
[Transportation Data Model](https://drive.google.com/file/d/0Bz18jufMWioiU25icDNoQWlJa2M/view),
[attribute descriptions and definitions](https://docs.google.com/document/d/1ojjqCa1Z6IG6Wj0oAbZatoYsmbKzO9XwdD88-kqm-zQ/edit),
and [download the Transportation Data Model schema](ftp://ftp.agrc.utah.gov/UtahSGID_Vector/UTM12_NAD83/TRANSPORTATION/UnpackagedData/Roads/_Statewide/UtahRoadsDataSchema/UtahRoadsDataSchema_gdb.zip).

Listed below are considered the minimum attributes:

| PREDIR | STREETNAME | STREETTYPE | SUFDIR |
| L_F_ADD | L_T_ADD | R_F_ADD | R_T_ADD |
| ALIAS1 | ALIAS1TYPE | ALIAS2 | ALIAS2TYPE |
| ACSALIAS | ACSNAME | ACSSUF | CLASS |
| MODIFYDATE | | | |

### [Address Points]({% link data/location/address-data/index.html %} "Address Points page"){: #address_points }

![Address Points]({% link images/90x90_address_points.png %}){: .pull-right .outline loading="lazy" }

View our
[Address Points Data Model](https://docs.google.com/document/d/1eTgknNbA0UNXnyMDR5q9gFAm0-XtNYQpLLYPSZtCLTU/edit?usp=sharing) and samples of [what they are used for]({% link downloads/Address_Point_Database_Values_V1_051914.pdf %}).
Listed below are considered the minimum attributes:

| Full Address (physical/situs)(ex. 622 N KAYCIE LN) | City | Zip Code | Parcel ID |

### [Parcels]({% link data/cadastre/parcels/index.html %} "Basic Parcels page"){: #parcels}

![Parcels]({% link images/90x90_parcels.png %}){: .pull-right .outline loading="lazy" }

The information below pertains to the _Basic Parcels_ however _Land Information Record Parcels_ (LIR) are also requested. More information about the LIR Parcels can be found on the [Work Group Recommends Expanded GIS Parcel Sharing]({% link _posts/2016-05-26-work-group-recommends-expanded-gis-parcel-sharing.md %}) page.

In addition to the parcel polygon geometry the following fields are a necessity and are considered the minimum attributes for the Basic Parcels:

| Parcel ID and/or Serial Number | Parcel Address (physical/situs)  _(this attribute is optional if accompanied by Address Points with a Parcel ID and/or Serial Number)_ |

### [Boundaries]({% link data/recreation/trails/index.html %} "Boundaries page"){: #boundaries }

![Boundaries]({% link images/90x90_voter_precincts.png %}){: .pull-right .outline loading="lazy" }

County and Municipal boundary changes should be submitted to the Lieutenant Governor's office and follow the requirements in state code. More information can be found on the [Utah Lieutenant Governor Municipal Certifications](https://municert.utah.gov/) website.

### [Building Footprints]({% link data/location/building-footprint/index.html %} "Building Footprints page"){: #building_footprints }

![Building Footprints]({% link images/90x90_building_footprints.png %}){: .pull-right .outline loading="lazy" }

This is a multi-purpose dataset of building footprint polygons for cartography and location purposes. The attributes below are optional:

| Name | Type | Address | Parcel ID | Source Year |

### [Trails]({% link data/recreation/trails/index.html %} "Trails page"){: #trails }

![Trails]({% link images/trail.png %}){: .pull-right .outline loading="lazy" }

View the [Trails Data Model](https://docs.google.com/spreadsheets/d/1OPGKmRrLYUBr9qO9EtbX6AwcRla82xMvc-BDr26ia9k/edit#gid=0). The following attributes are requested:

| Name | CartoCode |
