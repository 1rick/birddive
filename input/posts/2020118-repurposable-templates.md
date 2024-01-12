---

title: Thoughts on Repurposable Web Templates
categories: ["Side Projects"]
tags: ["Web Development"]

---



I'm still knocking around the idea of a (web-based?) static site generator in my head. And as part of that mental exercise, I thought I'd start at the end and work backwards with what the output HTML should look like. What would a versatile web template look like for a personal portfolio or small business site? 

**TL;DR:** [This is what I came up with.](https://1rick.github.io/mejiro-theme/)


Ideally a repurposable layout should be simple enough that it can work for almost any content. But what are the design choices that lead to a "repurposable" template? I'll touch on a few of those below.

As part of creating this little template, I had to study up on my CSS understanding a little bit, and dive into things like Flexbox and Grid that I hadn't really looked closely at before. In the interests of sharing, here are a few of the portions of CSS that I really liked, along with some comments on why I'm using them. For this template, I also avoided using any Javascript, partially because I need to study up on it, and also because I really want to stay as simple as possible. 

### 1. Root variables for setting theme colors

I'm sure any web designer worth their salt knows about these, and yet I rarely see them at the top of any CSS files I encounter in the wild. I'll use these to set my document colors, just so that they're easy to for any users to change (i.e. more "repurposable"), and in the interests of allowing for light and dark themes, I'll establish an easily swappable color-background and color-foreground variable as well. 




<pre><code>
:root {
  --primary-color: #00AEEF;
  --secondary-color: #cc5500;
  --page-background: ivory;
  --page-foreground: #333;
  }

</code></pre>


### 2. One-Column layout, with a limited line length for optimal readability

I've often seen complex template layouts created with multi-column content block, and those are perfectly fine -- but if you want to reuse them later, it might be tricky to make your content fit. So for this template, I'll stick to one-column, and in the interests of readability, let's not run it too wide. The [50 to 70 characters per line rule](https://baymard.com/blog/line-length-readability) is a best practice I see broken way too often on the web. And in the past I've used max-width of containers to enforce it, but thanks to Jeremy Thomas's brilliant little *[Web Design in 4 mins](https://jgthms.com/web-design-in-4-minutes/)*, let's use his recommendation of max-width: 50em along with some padding. We can set a line height of 1.5, and [leave it unitless](https://allthingssmitty.com/2016/12/26/add-line-height-to-body-copy/) in case any dependencies end up using different units. 

<pre><code>
#maincontent {
    margin: 0 auto;
    max-width: 50em;
    line-height: 1.5;
    padding: 4em 1em;
    color: var(--page-foreground);
}
</code></pre>



### 3. Full-bleed images by default, with option for narrow image constrained within the narrow body column

While I like the 50em width limitation for my body text, it's really nice to be able to break that constraint with images. So by default, let's make images full bleed, but retain the option of a "narrow_image" class to keep within the boundary. To do this, let's take a page from Kilian Valkov's and use the not() pseudo class to basically say, "anything that isn't an image or video within this *maincontent* container, keep it to 50rem wide". 


<pre><code>
#maincontent > *:not(img):not(video) { 
    max-width: 50rem;
    margin: auto;
  }

#maincontent img {
    max-width: 100%;
    display: block;
    margin: 3rem auto;
}
</code></pre>

For images that you don't want to extend for the full width, let's add that class as well using media queries. Because after all, on mobile, this narrow column will extend full width.

<pre><code>

@media screen and (min-width:800px) {

    #maincontent .narrow_image {
        max-width: 50rem;
    }
}
</code></pre>





### 4. Minimal interference with header background cover image

I like putting white text on darkened photos in my header sections, but applying dark overlays comes at the cost of fading the photo into the... um... background. A happy medium is applying a bit of a text shadow to assist with the contrast. And this leaves the photo a little more visible by default. The 'screen' background blending mode seems to darken the photo the least. If you need a little more, try 'overlay' or 'multiply'. 


<pre><code>
.hero {
    background-image: url("../images/header.jpg"), linear-gradient(rgba(0,0,0,0.2),rgba(0,0,0,0.2));
    background-blend-mode: screen;
    background-position: center;
    background-repeat: no-repeat;
    background-size: cover;
    line-height: 1.2;
    padding: 10vw 2em;
    text-align: center;
  }
</code></pre>




### Closing thoughts

You can see the template in action [here](https://1rick.github.io/mejiro-theme/). The files, if you'd like to download and mess about with them yourself, are [on Github](https://github.com/1rick/mejiro-theme/tree/gh-pages). I didn't intend for this to look like the old standard Wordpress Twenty Twenty theme, but it does remind me of that a little bit. As for the nav bar, that was a little tricky as I did start with a collapsed mobile view (borrowing some ideas from [here](https://www.youtube.com/watch?v=y4N-UeK0cJw)), with the media query declaring the "desktop view" for 800+ pixels. But I think it works well -- and there's no javascript involved. 



