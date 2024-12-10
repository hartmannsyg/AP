const puppeteer = require('puppeteer');

(async () => {
    try {
    const url = process.argv[2]
    const urlObj = new URL(url)
    const browser = await puppeteer.launch({
        args: [
            '--no-sandbox',
            '--disable-setuid-sandbox'
        ]
    });
    const page = await browser.newPage();
    
    await page.goto(url); 

    const delay = ms => new Promise(res => setTimeout(res, ms));
    await delay(5000)

    await browser.close();
}catch (e) {
    console.error(e)
}
})();