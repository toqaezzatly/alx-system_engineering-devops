---

# Postmortem: "The Case of the Phantom 500"

## Issue Summary

- **Duration:** August 16, 2024, 2:30 PM - 4:00 PM UTC  
- **Impact:** Our WordPress website decided to take a surprise vacation for 1.5 hours. During this period, 95% of users were treated to the mysterious "500 Internal Server Error" page, where all hopes of browsing were dashed. Both the public-facing site and admin dashboard were inaccessible. The outage resulted in missed content updates, frustrated users, and an impromptu coffee break for the dev team. 
- **Root Cause:** A mischievous typo in the `wp-settings.php` file where an extra "p" snuck into the file extensions, turning `php` into `phpp`. Unfortunately, Apache isn’t much of a guesser, so it simply threw its hands up and crashed.

## Timeline

- **2:30 PM UTC:** Monitoring alerts went off, indicating a significant spike in 500 errors across the site. The alert system lit up like a Christmas tree.
- **2:35 PM UTC:** The on-call engineer saw the alerts and confirmed that all HTTP requests were being met with 500 errors. Panic mode: engaged.
- **2:40 PM UTC:** Initial diagnostics focused on server health—CPU, memory, and disk space were all normal, hinting that the issue wasn’t hardware-related. We briefly entertained the idea that maybe the site just needed a coffee break.
- **2:50 PM UTC:** Apache logs revealed that the issue was coming from PHP include statements in `wp-settings.php`, but nothing in the logs pointed directly at what was wrong. Suspicion grew that a more sinister problem might be lurking.
- **3:00 PM UTC:** The "standard" fix was attempted: restarting the Apache server. If only our problems could all be solved with a simple reboot. But alas, no dice—the errors persisted.
- **3:10 PM UTC:** The PHP version and configuration were checked meticulously for any misconfigurations, but everything seemed fine. By this point, we were starting to think our web server was haunted.
- **3:20 PM UTC:** Senior developer brought in. After a few deep sighs and some caffeine, they combed through the `wp-settings.php` file. It didn’t take long for them to spot it—the villain of our story: `phpp` instead of `php`. Yes, we were brought down by a single extra "p".
- **3:40 PM UTC:** Puppet script deployed to hunt down and exterminate the extra "p" across the file using `sed`. We also took a moment to curse the existence of typos.
- **3:45 PM UTC:** Apache restarted. Error rate began dropping faster than our motivation during a Friday afternoon meeting.
- **4:00 PM UTC:** All services fully operational. Users could finally access the site again, and the dev team enjoyed a collective sigh of relief.

## Root Cause and Resolution

### Root Cause:
The root cause was embarrassingly simple: a typo in the `wp-settings.php` file where someone (we won’t name names) added an extra "p", turning `php` into `phpp`. This seemingly minor error led to WordPress failing to include critical PHP files, causing the entire site to throw 500 errors. Apache didn’t appreciate being handed fake file extensions and simply gave up.

### Resolution:
The resolution involved running a Puppet script that used the `sed` command to replace every instance of `phpp` with `php`. Once the typo was corrected, the Apache server was restarted, and the website immediately returned to normal. We celebrated this tiny victory with a round of nervous laughter and a reminder to double-check file paths next time.

## Corrective and Preventative Measures

### Lessons Learned:
1. **Typos Are No Joke:** A single mistyped character can send your website into oblivion. Always respect the mighty "p".
2. **Start with the Basics:** Don’t immediately assume the problem is a complex configuration issue. Sometimes, the simplest explanation is the right one—like a typo.
3. **Automate Fixes Where Possible:** Deploying a Puppet script saved us from manually combing through the code and ensured that similar issues can be automatically corrected in the future.

### Action Items:
- **Automated Code Validation:** Introduce a pre-deployment hook that checks for common typos and path errors in critical files before allowing changes to go live.
- **Improve Error Handling in Puppet Manifests:** Enhance the existing manifests to detect and alert on suspicious file extensions or include paths that don’t match expected patterns.
- **Extend Monitoring to Include Application-Specific Checks:** Implement monitoring that not only tracks 500 errors but also checks for specific patterns in log files that could indicate configuration or path issues.
- **Additional Training for Developers:** Encourage a healthy dose of paranoia when editing critical configuration files. A single extra character shouldn’t be the end of the world—but apparently, it can be.

---

In the end, this incident taught us that even in the world of high-tech web stacks, we can still be brought down by something as low-tech as a typo. If there’s a moral to this story, it’s that the smallest things can cause the biggest headaches. Here’s to better spelling, better monitoring, and hoping we never see that extra "p" again.

Cheers to debugging!
