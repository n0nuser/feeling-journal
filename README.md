<div id="top"></div>

# Monitor

Feeling Journal - Web App to register your thoughts and feelings!

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![GPL License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]


## Built With

[![Python][Python]][Python-url] [![Poetry][Poetry]][Poetry-url] [![Django][Django]][Django-url] [![Docker][Docker]][Docker-url] [![Uvicorn][Uvicorn]][Uvicorn-url] [![Nginx][Nginx]][Nginx-url]


<p align="right">(<a href="#top">back to top</a>)</p>


## Getting Started

### Installation and use

1. Modify the `.env` file to suit your needs.

```env
ALLOWED_HOSTS=127.0.0.1,YOUR-FQDN
DEBUG=True
DJANGO_SUPERUSER_EMAIL=account@gmail.com
DJANGO_SUPERUSER_PASSWORD=MY-USERNAME
DJANGO_SUPERUSER_USERNAME=MY-PASSWORD
EMAIL_HOST=smtp.gmail.com
EMAIL_HOST_PASSWORD=password
EMAIL_HOST_USER=account@gmail.com
EMAIL_PORT=587
POSTGRES_NAME=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_USER=postgres
SECRET_KEY=myDummySecretKey
SERVER_HOST=YOUR-FQDN
SERVER_PORT=80,443
```

2. Create the SSL certificates in the Nginx folder named `cert.pem` and `key.pem` for HTTPS to work. You can use [Certbot](https://certbot.eff.org/instructions) (web app uses Nginx).

3. Execute the `docker_compose_up.sh` file to deploy the containers.

```sh
chmod +x docker_compose_up.sh
./docker_compose_up.sh
```

<!-- ROADMAP -->
## Roadmap

Check the [Roadmap here](https://github.com/n0nuser/feeling-journal/issues/1).

See the [open issues](https://github.com/n0nuser/feeling-journal/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the GPL-3.0 License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Pablo González Rubio - [@n0nuser_](https://twitter.com/n0nuser_) - gonzrubio.pablo@gmail.com

Project Link: [https://github.com/n0nuser/feeling-journal](https://github.com/n0nuser/feeling-journal)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->

[contributors-shield]: https://img.shields.io/github/contributors/n0nuser/feeling-journal?style=for-the-badge
[contributors-url]: https://github.com/n0nuser/feeling-journal/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/n0nuser/feeling-journal?style=for-the-badge
[forks-url]: https://github.com/n0nuser/feeling-journal/network/members
[stars-shield]: https://img.shields.io/github/stars/n0nuser/feeling-journal?style=for-the-badge
[stars-url]: https://github.com/n0nuser/feeling-journal/stargazers
[issues-shield]: https://img.shields.io/github/issues/n0nuser/feeling-journal?style=for-the-badge
[issues-url]: https://github.com/n0nuser/feeling-journal/issues
[license-shield]: https://img.shields.io/github/license/n0nuser/feeling-journal?style=for-the-badge
[license-url]: https://github.com/n0nuser/feeling-journal/blob/main/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/nonuser

[Python]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[Python-url]: https://www.python.org/
[Poetry]: https://img.shields.io/badge/Poetry-3670A0?style=for-the-badge&logo=poetry&logoColor=ffdd54
[Poetry-url]: https://python-poetry.org/
[Django]: https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white
[Django-url]: https://www.djangoproject.com/
[Docker]: https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white
[Docker-url]: https://www.docker.com/
[Uvicorn]: https://img.shields.io/badge/uvicorn-%298729.svg?style=for-the-badge&logo=gunicorn&logoColor=white
[Uvicorn-url]: https://www.uvicorn.org/
[Nginx]: https://img.shields.io/badge/nginx-%23009639.svg?style=for-the-badge&logo=nginx&logoColor=white
[Nginx-url]: https://www.nginx.com/
