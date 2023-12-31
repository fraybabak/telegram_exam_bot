import jinja2


class ReportRepository:


    def create_report(self, report, template_name):
        template_loader = jinja2.FileSystemLoader(searchpath="src/templates")
        template_env = jinja2.Environment(loader=template_loader)
        template = template_env.get_template(template_name)
        output = template.render(report)



        return self.save_to_image(output, f"{report['campaign_id']}.png")

    def save_to_image(self, output, image_name: str):
        try:
            from html2image import Html2Image
            path_to_chrome = "/usr/bin/google-chrome-stable"
            hti = Html2Image(output_path="src/public/images", browser_executable=path_to_chrome, custom_flags=['--disable-gpu', '--no-sandbox', '--disable-software-rasterizer'])
            hti.screenshot(html_str=output, save_as=image_name, size=(1920, 1080))
    
            return f"src/public/images/{image_name}"


        except Exception as e:
            print("An error occurred:", e)
            raise e