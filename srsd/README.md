Dockermail - srsd
===
Once configured and linked to the `core`, this image will implement the Sender Rewriting Scheme (SRS), which allows you to forward without breaking the SPF.

See https://en.wikipedia.org/wiki/Sender_Rewriting_Scheme and http://www.openspf.org/SRS for the concept behind this.

The container setup follows very closely the [Ubuntu setup instructions of Ameir Abdeldayem](http://www.ameir.net/blog/archives/71-installing-srs-extensions-on-postfix-ubuntudebian.html), which in turn are based on [Christoph Fischer's article](http://christophfischer.com/linux/15-mailserver/56-sender-rewriting-scheme-srs-fuer-postfix-unter-debian), which references a [blog post by Benny Baumann](http://blog.benny-baumann.de/?p=388).

### Configuration

TBD

### To Do

1. Add support for multiple domains: https://github.com/Fruneau/pfixtools/issues/6
2. Read configuration (domain) from config.json.
3. Generate the srs secrets (`/etc/postfix/pfix-srs.secrets`) on first run, but not if they are already in the volume.
4. Finish documentation.
