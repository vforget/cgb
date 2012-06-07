cgb -- create custom instances of the UCSC Genome Browser
=========================================================

CONTENTS
--------
/A SUMMARY
/B USAGE
/C EXAMPLES
/D AUTHOR
 
/A SUMMARY
cgb is a bash script to automate the creation of password-protected instances 
of the UCSC Genome Browser.  The goal is to rapidly create UCSC Genome Browser 
(http://www.genome.ucsc.edu) instances for non-reference genomes.

It requires that the UCSC Genome Browser framework (sans genome data) is installed.

Full documentation is forthcoming.  For more information please contact:

vincenzo.forgetta at mail.mcgill.ca

Copyright (C) 2011,2012  Vincenzo Forgetta, Pascale Marquis

"cgb" is released under the GPLv2 license; see LICENSE.txt for more
info.

/B USAGE

The usage of cgb can be divided into the following sections (see below for more information):

* Setup the browser space: extract binaries for browser, setup apache password, create 
  hgcentral for the client.
* Add entry to the clade pulldown menu: add entry to hgcentral database.
* Add entry to the genome pulldown menu: add entry to hgcentral database.
* Add entry to the build pulldown menu: add entry to hgcentral database.
* Add entry to the defaultdb table (i.e. which genome build is the default one): add entry to 
  hgcentral database.
* Add build sequence and annotations
  - add_454: sort contigs by length to create a chromosome, create tracks for GC percent, 
    read depth, contigs and gaps.
  - add_fasta: for non-454 assemblies i.e. a fasta file with a chromosome sequence. Creates 
    track for GC percent only.
  - add_454_scaffold: sort scaffolds by length to create genome build, create tracks 
    for GC percent, read depth, contigs and gaps, and scaffolds.
* Add BLAT servers: add entry for DNA and translated BLAT to hgcentral database. Start BLAT servers at specified port numbers.

NOTE: When adding BLAT servers, be sure to use port numbers above 1024.

Each section has methods to add, remove and list entries (see below).

$ cgb
cgb -- a program to a create custom instance of the UCSC Genome Browser.
         NOTE:
           Reset the CLIENT_NAME for the current session: export CLIENT_NAME=DrWatson
           All COMMANDs are specific to CLIENT_NAME.
         COMMAND          ARGUMENTS -- Description
         -------          ------------------------
         create_browser   no arguments -- Create a browser instance.
         remove_browser   no arguments -- Remove a browser instance.
         add_clade        CLADE_LABEL CLADE_NAME PRIORITY -- add a clade entry to pulldown menu.
         remove_clade                 CLADE_NAME          -- remove a clade entry.
         list_clade       List clades.
         add_genome       GENOME CLADE_NAME PRIORITY -- Add a genome entry to pulldown menu.
         remove_genome    GENOME                     -- Remove a genome entry.
         list_genome      List genomes.              -- List genomes.
         add_build        BUILD BUILD_DESC GENOME CHROM SPECIES SOURCE TAXID -- Add a genome build to the browser.
         add_454          BUILD CHROM ASSEMBLY_DIR                     -- Add 454 assembly contigs to a build.
         add_454_scaffold BUILD CHROM ASSEMBLY_DIR                     -- Add 454 assembly scaffolds to a build.
         add_fasta        BUILD CHROM FASTA_FILE                       -- Add a fasta file to a build.
         remove_build     BUILD                                        -- Remove a build.
         list_build       List builds.
         add_defaultdb    GENOME BUILD -- Add the a defaultDb entry to pulldown menu.
         remove_defaultdb        BUILD -- Remote a defaultDb entry.
         list_defaultdb   List defaultDbs.
         add_blat         BUILD BLAT_PORT1 BLAT_PORT2. Create and load BLAT servers.
         remove_blat      BUILD BLAT_PORT1 BLAT_PORT2. Remove and unload BLAT servers.
         list_blat        List BLAT servers.
         add_depth        BUILD CHROM ASSEMBLY_DIR                     -- Add depth to a build.
         --help           Print this message.
/C EXAMPLES
$ export CLIENT_NAME=TestClient
$ cgb create_browser
$ cgb add_clade 'E. coli' ecoli 1
$ cgb add_genome K12 ecoli 1
$ cgb add_defaultdb K12 ec1
$ cgb add_build ec1 Build1 K12 chrI "E. coli strain K-12" "MUGQIC/NCBI" 562
$ cgb add_454 ec1 chrI /path/to/454/assembly
$ cgb add_blat ec1 12345 12346

An example of a custom *C. difficile* UCSC Genome Browser can be found at:

http://www.genomequebec.mcgill.ca/compgen/browser/cgi-bin/hgGateway

/D AUTHOR
Written by Vince Forgetta.
