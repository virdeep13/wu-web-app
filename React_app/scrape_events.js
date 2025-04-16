const puppeteer = require('puppeteer');
const he = require('he');

async function scrapeEvents() {
  const browser = await puppeteer.launch({headless:true});
  const page = await browser.newPage();
  try{
    // Log that the scraping process has started
    console.log('Starting to scrape events from Widener University');

  
  await page.goto('https://www.widener.edu/events', { waitUntil: 'networkidle2' });
  await page.waitForSelector('article.event-listing__item');
  console.log('Event listings loaded.');
  const events = await page.evaluate(() => {
    return Array.from(document.querySelectorAll('article.event-listing__item')).map(event => ({
      date: event.querySelector('.columns.shrink')?.innerText.trim() || 'No date',
      details: event.querySelector('.event-listing__details')?.innerText.trim() || 'No details',
      open_to:event.querySelector('.event-listing__open-to')?.innerText.trim() || 'No open-to info',
      description: event.querySelector('.event-listing__item__text')?.innerText || 'No description'
    }));
  });
const decodedEvents = events.map(event => ({
    //const decodedOpenTo = he.decode(event.open_to);
  //await browser.close();
  //return events;
//}..
  date: he.decode(event.date),
  details: he.decode(event.details),
  open_to: he.decode(event.open_to),
  description: he.decode(event.description)
//return{//const decodedEvents = events.map(event => ({
  
//}));
}));
console.log('Scraping completed successfully!');
return decodedEvents ; 
}catch (error){
  // Handle any errors that occur during the scraping process
  console.error('Error during scraping:', error);
  return [];  // Return an empty array if scraping fails
 }finally {
  // Always close the browser regardless of success or failure
  await browser.close();
  console.log('Browser closed.');
  }
}
module.exports = scrapeEvents;
