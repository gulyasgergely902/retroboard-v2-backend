# RetroBoard

A lightweight, full-stack application for running productive sprint retrospective ceremonies. Built with Python 3, Flask, SQLAlchemy, and a Vue 3 frontend, this app enables team members to anonymously write and later share feedback and ideas about the last sprint.

## What it Does

Built with collaborative teams in mind for an efficient retrospective ceremony:

- 🧠 **Write your thoughts in private**: Everyone can write down their feedback about the last sprint — but you won’t see what others wrote until everyone is ready to discuss. This keeps the input unbiased and personal.
- 👀 **Reveal mode when it's time to discuss**: Once everyone’s done writing, we switch to a reveal page that shows all the ideas for group discussion.
- 🚀 **Fast, clean, no clutter**: Just the essentials — no logins, no bloat, no distractions. Open the link, write your thoughts, done.
- 🔐 **Fully self-hosted**: You can run it on your own servers or environment, so you stay in control of your data — perfect if your company has privacy or security policies.

## The tech behind

- **Backend**: Built with Python 3 using Flask & SQLAlchemy.
- **Frontend**: Vue 3 to make the tool fast and simple.
- **Database**: Using SQLite to store the data locally — where it belongs.

## Using to tool

This is cool, but how should I use it? Here is a simple breakdown:

1. Before starting the retrospective meeting, create a new board for your thoughts. Everyone at the meeting will add their ideas to this.
2. When the meeting starts, everyone opens the app and writes their feedback to different categories from the last sprint. Don't worry, no-one can see these at this stage, yet.
3. After the team finished adding new ideas, the faciliator of the meeting reveals the notes and the team checks them together.

## How to run it

The tool lives in a docker container to simple things even futher. It needs to be hosted on your server and expose it to the network, the application will take care of the rest. Make sure you either expose port `8000` or re-route it as you like.

Here is an example:
```docker run --rm -ti -p 8000:8000 retroboard:latest```

## Build from source

In rare cases when you want to build it from the source, it is not any harder.

1. Build the frontend using `build-frontend.sh`.
2. Create a virtual environment.
3. Install the required modules in the environment which are needed to run the app.
4. Run the app using `run.py` inside the folder `src/`.

## Contribution

If you find any bugs or just have an idea for the last missing feature, create a ticket here on GitHub and I'll take care of the rest!
