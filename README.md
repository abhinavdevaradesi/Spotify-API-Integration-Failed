# Spotify API Integration - Partial Work (Failed Attempt)

## What is this?

This repo contains my attempt to integrate with the Spotify API to fetch audio features for top tracks.

## What I tried

- Used Spotipy library with OAuth authentication.
- Fetched user’s top tracks from Spotify.
- Attempted to get detailed audio features for these tracks in batches.
- Saved results into CSV files for further analysis.

## What went wrong

- Hit frequent HTTP 403/401 errors related to API authentication and scope permissions.
- Spotify API rate limits caused intermittent failures.
- Handling expired tokens and batch requests proved unreliable.
- Despite multiple retries and debugging, I could not get stable audio features retrieval.

## What I learned

- API integration requires solid token management and scope handling.
- Public APIs can be unreliable and sometimes require fallback plans.
- Debugging API failures is part of real-world dev and data engineering.
- Need to build robust error handling and logging mechanisms.

## Next steps

- Switching focus to publicly available music datasets (Million Song Dataset, Free Music Archive, etc.) for stable and scalable analysis.
- Plan to build an audio features dashboard using static data before attempting live API integration again.
- Will revisit Spotify API integration after strengthening core data handling skills.

---

Feel free to browse the code and reach out if you want to discuss!

---

**Author:** Abhinav Devaradesi

**Date:** 06-06-2025

