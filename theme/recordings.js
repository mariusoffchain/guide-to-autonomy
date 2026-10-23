/*
 * A Guide to Autonomy, player of the talk recordings on the cover (only when edition.json enables recordings).
 * Copyright (C) 2026 the contributors of A Guide to Autonomy. AGPL-3.0-or-later, see LICENSE.
 *
 * Without JavaScript the button and the poster are plain links to the recording. With it, a click creates the
 * player in place: a <video> for a video file (the browser takes the first source it can play), or a
 * youtube-nocookie.com frame for a YouTube address. Nothing is requested from another site before that click.
 * The pages send no referrer; only the clicked YouTube frame sends this site's origin, which YouTube requires.
 */
(function () {
  'use strict';
  const YT = /^https:\/\/(?:www\.)?(?:youtube\.com\/(?:watch\?v=|embed\/|shorts\/)|youtu\.be\/)([A-Za-z0-9_-]{6,})/;
  document.querySelectorAll('.rp-item[data-video]').forEach((li) => {
    const d = li.dataset;
    const title = li.querySelector('.rp-title');
    const label = title ? title.textContent : 'Video';
    const yt = d.video.match(YT);
    const play = (e) => {
      e.preventDefault();
      if (li.classList.contains('rp-playing')) return;
      const box = document.createElement('div');
      box.className = 'rp-embed';
      let player;
      if (yt) {
        player = document.createElement('iframe');
        player.src = 'https://www.youtube-nocookie.com/embed/' + yt[1] + '?autoplay=1&rel=0';
        player.referrerPolicy = 'strict-origin-when-cross-origin';
        player.title = label;
        player.allow = 'autoplay; encrypted-media; picture-in-picture';
        player.allowFullscreen = true;
      } else {
        player = document.createElement('video');
        player.controls = true;
        player.playsInline = true;
        player.preload = 'auto';
        player.setAttribute('aria-label', label);
        const thumb = li.querySelector('.rp-thumb img');
        if (thumb) player.poster = thumb.src;
        [[d.video, d.videoType], [d.videoSd, d.videoSdType]].forEach(([src, type]) => {
          if (!src) return;
          const s = document.createElement('source');
          s.src = src;
          if (type) s.type = type;
          player.appendChild(s);
        });
      }
      box.appendChild(player);
      li.appendChild(box);
      li.classList.add('rp-playing');
      player.focus();
      if (player.play) player.play().catch(() => { /* the reader presses play */ });
    };
    li.querySelectorAll('.rp-play, .rp-thumb').forEach((a) => a.addEventListener('click', play));
  });
}());
