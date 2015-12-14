# Embedded-ember

An example of how to transition a server side rendered application to an API driven, front-end application.

This allows for parts of the old application to be converted to Ember components as they are developed.

This example project uses a Django site on the back end with the Ember application being hosted on S3. Some configuration is specific to these choices.

## Ember addons

Several addons are used to enable this functionallity. Two of them are not installed by default on a new ember cli application.

* [ember-islands](https://github.com/mitchlloyd/ember-islands)
* [ember-cli-embedded](https://github.com/xcambar/ember-cli-embedded)

## Steps

1. Install the addons
2. Update the configration
3. Add example component
4. Profit

### Install the addons

Run `ember install ember-islands`  
Run `ember install ember-cli-embdded`  

### Update the configuration

The name of the ember application cooresponds with the [Django templatetag](https://github.com/imtapps/embedded-ember/blob/django-template-tag/s3test/trythis/templatetags/s3.py)

1. Change `bower.json` to use the Ember and jQuery 2.0 branches
2. Run `bower install`
3. Update `ember-cli-build.js`
4. Update `config/environment.js`

### Add example component

The component name corresponds with the [Django template](https://github.com/imtapps/embedded-ember/blob/django-template-tag/s3test/trythis/templates/index.html)

1. Run `ember g component imt-text`
2. Add computed property to component
3. Add text, image, and property component's handlebars file

### Profit

1. Build ember with `ember build -prod`
2. Upload `dist/assets` to the S3 bucket
3. Start Django application (for this example checkout the `django-template-tag` branch and follow the directions)
4. Profit because you began your conversion to an ember application without taking two years to redevelop everything at once

#### Dependencies

For those concerned about dependencies:

* [ember-islands](https://github.com/mitchlloyd/ember-islands/blob/master/package.json)  
  └[ember-cli-version-checker](https://github.com/rwjblue/ember-cli-version-checker/blob/master/package.json)  
  &nbsp;&nbsp;└[semver](https://github.com/npm/node-semver/blob/master/package.json)  

* [ember-cli-embedded](https://github.com/xcambar/ember-cli-embedded/blob/master/package.json)  
  ├[ember-export-application-global](https://github.com/ember-cli/ember-export-application-global/blob/master/package.json)  
  └[ember-cli-babel](https://github.com/babel/ember-cli-babel/blob/master/package.json)  
    &nbsp;&nbsp;└[several that are not shown for brevity](https://github.com/babel/ember-cli-babel)  


# All follows is the stock ember readme

## Prerequisites

You will need the following things properly installed on your computer.

* [Git](http://git-scm.com/)
* [Node.js](http://nodejs.org/) (with NPM)
* [Bower](http://bower.io/)
* [Ember CLI](http://www.ember-cli.com/)
* [PhantomJS](http://phantomjs.org/)

## Installation

* `git clone <repository-url>` this repository
* change into the new directory
* `npm install`
* `bower install`

## Running / Development

* `ember server`
* Visit your app at [http://localhost:4200](http://localhost:4200).

### Code Generators

Make use of the many generators for code, try `ember help generate` for more details

### Running Tests

* `ember test`
* `ember test --server`

### Building

* `ember build` (development)
* `ember build --environment production` (production)

### Deploying

Specify what it takes to deploy your app.

## Further Reading / Useful Links

* [ember.js](http://emberjs.com/)
* [ember-cli](http://www.ember-cli.com/)
* Development Browser Extensions
  * [ember inspector for chrome](https://chrome.google.com/webstore/detail/ember-inspector/bmdblncegkenkacieihfhpjfppoconhi)
  * [ember inspector for firefox](https://addons.mozilla.org/en-US/firefox/addon/ember-inspector/)
