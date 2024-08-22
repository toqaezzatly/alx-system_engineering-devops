# Web Stack Debugging #4: When the Sky Isn't the Limit

## Project Overview
Welcome, fellow tech adventurers! In this project, we’re on a mission to push our Nginx web server to its limits and beyond—literally. You’ll be debugging a web stack that’s screaming for help under pressure. If the words “failed requests” and “server stress” sound like a challenge rather than a nightmare, you’re in the right place. Let’s dive into the wonderful world of Puppet manifests and see if we can make those error logs a thing of the past.

## Installation Instructions
Before we dive into the nitty-gritty, make sure your setup is ready to go. Here's what you’ll need:

1. **Operating System**: Ubuntu 14.04 LTS (the OG classic).
2. **Puppet Version**: v3.4 (because we’re keeping it old school).
3. **puppet-lint Version**: 2.1.1 (because lint-free code is happy code).

Run the following commands to get started:

```bash
apt-get install -y ruby
gem install puppet-lint -v 2.1.1
```

And voila, you’re ready to rock!

## Tasks

### 0. Sky is the Limit, Let's Bring That Limit Higher

Our first task is to stress-test our Nginx web server using **ApacheBench** (aka "AB"). We’re simulating a whopping 2000 requests with 100 requests at a time. The results? Not great—our server is struggling and throwing out 943 failed requests. 

But don’t worry, that’s where the magic of Puppet comes in! We’re going to tweak our server’s configuration to make those errors disappear faster than your weekend plans.

Run your Puppet manifest like so:

```bash
puppet apply 0-the_sky_is_the_limit_not.pp
```

After that, run the benchmark test again and watch the errors drop to zero! You’ll feel like you just pulled off a high-stakes heist, but instead of money, you got a perfectly running web server.

### 1. User Limit? Ain't Nobody Got Time for That

Imagine trying to log in with your user account, and the system responds with: *"Too many open files!"* Talk about hitting a wall. But fear not! We’re about to show this OS who’s boss.

This task fixes the login issues by adjusting the system configuration for the user. Run this Puppet manifest:

```bash
puppet apply 1-user_limit.pp
```

Now you can log in without the system whining about file limits. It’s like telling your OS, “Chill out, I got this.”

## Why This Matters
Debugging web stacks under pressure is what separates the rookies from the pros. Learning how to fix these issues will make you the hero your servers deserve. And with Puppet, it’s all about making your life easier, one manifest at a time.

---

Happy debugging, and remember: logs are your best friends when everything goes wrong (which they always do). Now, go forth and conquer those failed requests with style!
