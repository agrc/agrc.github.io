---
title: GIS - Thinking Beyond the Map
author:
  display_name: Greg Bunce
  email: gbunce@utah.gov
date: 2020-07-14 10:07:46
categories:
  - Featured
tags:
  - gis
  - data
  - coordination
---

If you’re reading this post, you’re already aware that geospatial technology (a.k.a. GIS) has become an essential part of our daily lives. Its capabilities extend from small-scale phone applications all the way up to multibillion dollar business systems, including big tech, insurance, intel and healthcare industries, just to name a few. As a result, the distinction between information technology and GIS is fading fast. This is exciting because as geospatial technology goes mainstream, we are seeing a wider array of uses for it - and often, the map is nowhere to be seen. It’s the invisible geospatial data and intelligence that is driving these systems.

![Location drives the system]({% link images/geospatial.png %})[^location]
{: .flex .flex--center}

### Where's the map?
{: .text-left}

Next Generation 911 (NG911) offers a good example of an invisible GIS. In NG911 systems, GIS is used to determine the caller’s location and then to use that location to determine which 911 center the call will be directed to. In other words, when an emergency call is placed from a landline, GIS is used to convert the caller’s address into geographic coordinates and then to use those coordinates to find which 911 center’s boundary the caller is located within. If 911 is called from a cell phone, the caller’s location is determined on-the-fly from the phone’s GPS, or from triangulation between the nearest cell phone tower’s geographic coordinates. No traditional maps are consulted during this process. Yet, the invisible, map-based data and GIS calculations are what connect you to the critical help you need.

GIS now plays an integral part in many voting systems. Many election departments are using GIS to maintain voter information and create informative election maps, but increasingly they are using GIS to generate election ballots as well. In this use case, a voter’s address is intersected with the appropriate election boundaries to determine what offices and questions will appear on an individual voter’s ballot. Again, the output here is not a map but, rather, a ballot. Similar to how spatial relationships drive NG911, GIS is also playing a key invisible role in election ballots.

Another example of where geospatial technology is predominant is on our personal and voice-enabled devices. On these platforms, the map is often complementary if shown at all. This is particularly true as we build more complex applications and ‘skills’ that allow us to more naturally interact with them. For example, think about the question, “What’s the weather today?” In this case, we need to know the device’s location as well as the nearest weather station. GIS handles the details, but ultimately we’re only concerned with getting the forecast.

![Voice queries]({% link images/voice-queries.png %})[^voice]
{: .flex .flex--center }

There are countless other questions that GIS can help answer: What day is my garbage pickup? What is the air quality today? Where am I? GIS is the engine that processes these queries, but the desired results are text based. For instance, to answer that last example question (i.e., Where am I?), reverse geocoding would return a human-readable civic address.

### What's next?
{: .text-left}

The use of GIS continues to evolve, and the benefits of the technology are becoming more ingrained in what we come to expect as “normal.” As systems become more complex, the next wave of geospatial applications will increasingly consume data from multiple sources in a variety of formats. In addition to location, an application might pull data from the nearest weather service; the public alert system (e.g., for information about road closures, local events, and natural hazards); and our personal data, such as average walk speed, travel patterns, and calendars and pictures. Additionally, these applications will incorporate artificial intelligence and machine learning “on-the-fly” to interpret features on the ground, such as the existence of restrooms at a park or the location and density of shade trees.

![What's next in geospatial?]({% link images/geospatial-whats-next.png %}){: .outline }[^geospatialnext]
{: .flex .flex--center }

Putting this all together, it's easy to envision a dialogue with a device that might sound something like this...

> Human: How should I prepare for Thomas's birthday tomorrow?
>
> Device: Tomorrow at Sugarhouse Park it will be sunny in the afternoon, but there are plenty of shade trees. Expect rain in the morning, so bring an umbrella, but there are ample pavilions for shelter on the north end. The park does have restrooms. Also, there is a half-marathon scheduled, which might affect your route. How do you plan to get there?

As convenient as this sounds, this concept teeters between creepy and cool. Ultimately though, it will most likely be our comfort levels, and not technical ability, that influence the next wave of geospatial applications and skills.

### Data is the foundation
{: .text-left}

Geospatial data is now more important than ever. It’s the bridge between GIS professionals and countless other industries. It’s the foundation that allows us to work together and speak the same language. A map, whether it’s present or not, is a cartographic representation of the data. But, it’s the data itself that connects us and powers our complex solutions.

![location data]({% link images/location-data.png %}){: .outline }[^locationdata]
{: .flex .flex--center}

It's been said that “data is the new oil”, but I would add that “data is the oil to the engine”[^bhageshpur],[^economist],[^toonders]. This makes it critical that we, as a GIS community, create quality data. The data we create today will be used to solve tomorrow's problems, and successful solutions depend on quality data.

### The role of GIS professionals
{: .text-left}

As geospatial data and services become more widely used, GIS professionals should see this as an opportunity to reach out to our diverse communities and pave the path forward together. In doing so, we should strive to reach the following goals:

![Collaboration]({% link images/collaboration.jpg %})[^collaboration]
{: .flex .flex--center}

- Bridge the Gap between IT and GIS
  - GIS and IT are no longer two separate industries/entities. Moving forward, we need to see ourselves seated in the same room, speaking the same language, and working together to provide seamless solutions and services to our customers. This approach encourages not only cross-pollination but also the formation of fresh, new ideas.

- Use APIs and Ensure Open Data
  - Our data should be open and usable to GIS and non-GIS users alike. The next wave of GIS will be built for applications and skills that rely heavily on APIs and [open data](https://opendatahandbook.org/guide/en/what-is-open-data/). Offering APIs allows us to expose our data to simple web queries. Additionally, as we open our data to a broader audience, it’s important that we are adhering to industry standards and conventions, such as uniform web standards described by the World Wide Web Consortium (W3C) and the Open Geospatial Consortium (OGC). Adhering to these standards guarantees that our data is open and usable.

- Continue Coordination and Partnership Efforts
  - As we move into the next era of GIS, it’s critical that we are moving forward collectively. This can be achieved by coordinating our efforts with other agencies and also collaborating with the public. The goal is to collectively build shared resources when appropriate and possible.

  These relationships help us understand where we overlap and, therefore, where we can work together. Often, this leads to the creation of better, more-accurate authoritative data and services.

- Decentralize Data, Services, and Other Resources
  - As GIS further integrates into information technology, we need to embrace the idea that applications and skills are consuming data and services from a variety of sources. In a sense, these external dependencies create a level of vulnerability. However, it’s important that we create partnerships and relationships that allow us to understand shared goals, set expectations, and ultimately minimize unexpected results.

### From maps to geospatial
{: .text-left}

Now more than ever, our data is being used among a diverse set of industries and users. It brings to mind the sentiments of Ed Parsons, geospatial technologist of Google, when he said, “We need to recognize that 95% of the consumers of whatever we create will not be GIS specialists”[^gim]. While that percentage may vary within our organizations, it's certainly a notion to embrace.

While traditionally we think of GIS as a tool for making maps and creating and maintaining spatial data, it has become much more. It’s time to start thinking beyond the map.

### What is UGRC doing?
{: .text-left}

![UGRC supports geospatial]({% link images/agrc-supports-geospatial.png %}){: .outline }[^tribolet]
{: .flex .flex--center}

#### Links related to UGRC's efforts

- [Partnerships and Sharing]({% link sharing/index.md %})
- [Data sharing Initiatives - Farm to AGOL project]({% link sharing/index.md %}#open-data)
- [State Geographic Information Database (SGID) - data index]({% link data/index.html %})
- [Open Data - SGID ESRI Hub site](https://opendata.gis.utah.gov/)
- [Open SGID - PostgreSQL/PostGIS cloud SGID database]({% link _posts/2020-05-04-introducing-open-sgid.md %})
- [UGRC Web API](https://api.mapserv.utah.gov/)
- [GitHub code and project repositories](https://github.com/agrc)
- [Utah Department of Technology Services' Citizen Portal project](https://demosite.utah.gov/citizen-portal/written-plans/next-generation-portal/)
- [UGRC Innovation Grant for Digital Assistant Skills]({% link _posts/2019-05-30-thoughts-from-teaching-google-and-amazon-new-skills.md %}), [Overview of the Grant]({% link _posts/2018-09-11-agrc-innovation-award-grant.md %})

#### Sources
{: .text-left}

[^gim]: GIM International. 2015. "Bringing Geography into Everything". https://www.gim-international.com/content/news/bringing-geography-into-everything-gim-international-interviews-ed-parsons (accessed February 13, 2020).

[^location]: gimbal https://gimbal.com/location-data-guide/

[^voice]: vectorified https://vectorified.com/download-image#voice-command-icon-4.jpg

[^geospatialnext]: fashionretail. https://fashionretail.blog/2018/06/11/internet-of-things-in-fashion/

[^locationdata]: 123rf. https://www.123rf.com/photo_75188771_stock-vector-black-binary-code-on-white-background-algorithm-binary-data-code-decryption-and-encoding-row-matrix-.html

[^economist]: The Economist. 2017. "[The world’s most valuable resource is no longer oil, but data](https://www.economist.com/leaders/2017/05/06/the-worlds-most-valuable-resource-is-no-longer-oil-but-data)". The Economist. May 6, 2017.

[^toonders]: Toonders, Joris. 2014. "[Data Is the New Oil of the Digital Economy](https://www.wired.com/insights/2014/07/data-new-oil-digital-economy/)". Wired. July 2014.

[^collaboration]: tapetapnetworks. https://www.taptapnetworks.com/bridging-the-gap-the-next-frontier-for-mobile-and-physical-commerce/

[^bhageshpur]: Bhageshpur, Kiran. 2019. "[Data Is The New Oil - And That's A Good Thing](https://www.forbes.com/sites/forbestechcouncil/2019/11/15/data-is-the-new-oil-and-thats-a-good-thing/#1d3b1a037304)". Forbes. Nov 15, 2019.

[^tribolet]: Tribolet, Anna. 2020. "What is UGRC Doing to Support the Next Wave of Geospatial Technology?". State of Utah, Department of Technology Services.
