---
status: publish
layout: page
tags:
  - dem
  - lidar
  - elevation
author:
  display_name: Rick Kelson
  email: rkelson@utah.gov
published: true
date: 2020-07-05 12:30:30
title: 2020 Northern & Central Utah Lidar Elevation Data
categories: []
---

![Sample]({% link images/lidar_northern_central_utah_2020.png %}){: .flex .flex--center .outline }

[![Project area map]({% link images/lidar_northern_central_utah_2020_coverage_sm.png %} "click for map")]({% link images/lidar_northern_central_utah_2020_coverage.png %}){:.inline-text-right}

{%- capture contact -%}
{%- include contact.html subject=page.title contact=site.data.contacts.elevation text='or by request from' -%}
{%- endcapture -%}
During 2020 UGRC, the Natural Resource Conservation Service (NRCS), and the Utah Division of Emergency Management acquired [~5,262 square miles]({% link images/lidar_northern_central_utah_2020_coverage.png %}) of 2 and 8 points per meter Quality Level 1 & 2 LiDAR of portions of Northern and Central Utah. The .5 and 1 meter resolution bare earth DEMs and first-return/highest-hit DSMs in .tif format have a 10.0cm vertical RMSE accuracy and are available for download. The LAS point clouds are available from [The National Map](https://apps.nationalmap.gov/downloader) {{ contact }} This elevation data was collected between April and July, 2020.

<ul class="dotless">
  <li>
    <strong>
      {% include fa_icon.html download=true class="svg-inline--fa fa-w-16" %} <a href="https://raster.utah.gov/?catGroup=.5%20Meter%20%7B2020%20Northern%20Central%20Utah%20LiDAR%7D,1%20Meter%20%7B2020%20Northern%20Central%20Utah%20LiDAR%7D&title=Northern%20Central%20Utah%202020%20LiDAR" target="_blank">Retrieve 2020 Bare Earth DTMs and First Return DSMs via Interactive Map</a>
    </strong>
  </li>
  <li>
    {% include fa_icon.html download=true class="svg-inline--fa fa-w-16" %} Download project <a href="https://storage.googleapis.com/state-of-utah-sgid-downloads/lidar/northen-central-utah-2020/NorthernCentralUtah_2020_Reports.zip" target="_blank">Reports</a> and <a href="https://storage.googleapis.com/state-of-utah-sgid-downloads/lidar/northen-central-utah-2020/NorthernCentralUtah_2020_Metadata.zip" target="_blank">Metadata</a>
  </li>
  <li>
    {% include fa_icon.html download=true class="svg-inline--fa fa-w-16" %} Download <a href="https://storage.googleapis.com/state-of-utah-sgid-downloads/lidar/northen-central-utah-2020/NorthernCentralUtah_2020_shps.zip" target="_blank">shapefiles</a> of project area, tile indices, and breaklines
  </li>
</ul>

The naming convention for the tiles are based off the [U.S. National Grid (USNG)](https://www.fgdc.gov/usng/how-to-read-usng/index_html).

This elevation data has a UTM NAD83 (2011) zone 12 north meters NAVD88(GEOID12) projection with the exception of a small strip on the western edge of the project area in zone 11.

{% include contact.html subject=page.title contact=site.data.contacts.elevation %}
