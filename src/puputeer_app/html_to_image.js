const puppeteer = require('puppeteer');
const fs = require('fs').promises;


(async () => {
    try {
        const browser = await puppeteer.launch({
            headless: true, args: ['--no-sandbox', '--disable-setuid-sandbox'], defaultViewport: {
                width: 1920,
                height: 1080
            }
        });

        const page = await browser.newPage();
        // await page.setViewport({ width: 1920, height: 1080 });
        const htmlFilePath = process.argv[2];
        const output_path = process.argv[3];
        const htmlContent = await fs.readFile(htmlFilePath, 'utf8');
        await page.setContent(htmlContent);
        await page.waitForNetworkIdle({ waitUntil: 'networkidle0' });
        // await page.pdf({ path: output_path, format: 'A4' })
        await page.screenshot({ path: output_path, fullPage: true });
        await browser.close();
    } catch (e) {
        console.log(e);

    }

    // await page.pdf({ path: pdfFilePath, format: 'A4' })
})();
