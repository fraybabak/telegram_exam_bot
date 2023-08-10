import jinja2
import subprocess
class ReportRepository:

    def create_report(self, report, template_name):
        template_loader = jinja2.FileSystemLoader(searchpath="src/templates")
        template_env = jinja2.Environment(loader=template_loader)
        template = template_env.get_template(template_name)
        output = template.render(report)
        html_file_path = "src/public/html/report.html"
        with open(html_file_path, "w") as file:
            file.write(output)

        return self.save_to_image(html_file_path, "src/public/images/1.png")

    def save_to_image(self, html_file_path: str, image_file_path: str):
        try:
            result = subprocess.run(['node', 'src/puputeer_app/html_to_image.js', html_file_path, image_file_path], capture_output=True, text=True)
            if result.returncode != 0:
                print("An error occurred:", result.stderr)
            else:
                print("image successfully created", result.stdout, result.stderr)
            return image_file_path


        except Exception as e:
            print("An error occurred:", e)
            raise e