#include <mgba/core/core.h>
#include <mgba/core/interface.h>
#include <mgba-util/vfs.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/* Direct core test: no Qt, X11, audio device or wall-clock input. */
static color_t pixels[240*160];
static uint64_t hash(void) {
    uint64_t h=1469598103934665603ULL;
    for(unsigned i=0;i<240*160;i++){h^=pixels[i];h*=1099511628211ULL;}
    return h;
}
static void frames(struct mCore *c,unsigned n,unsigned keys) {
    c->setKeys(c,keys);
    for(unsigned i=0;i<n;i++) c->runFrame(c);
    c->setKeys(c,0);
}
int main(int argc,char **argv) {
    if(argc!=2) return 2;
    struct mCore *c=mCoreFind(argv[1]);
    if(!c || !c->init(c)) return 3;
    mCoreInitConfig(c,NULL);
    c->setVideoBuffer(c,pixels,240);
    if(!mCoreLoadFile(c,argv[1])) return 4;
    c->reset(c);
    frames(c,600,0);
    uint64_t first=hash();
    frames(c,120,0);
    uint64_t second=hash();
    frames(c,1,8); /* GBA Start */
    frames(c,120,0);
    uint64_t third=hash();
    frames(c,1,1); /* GBA A */
    frames(c,120,0);
    uint64_t fourth=hash();
    if(first==second && second==third && third==fourth) {
        fprintf(stderr,"No framebuffer changes across boot/input sequence\n"); return 5;
    }
    size_t n=c->stateSize(c);
    void *state=malloc(n);
    if(!state || !n || !c->saveState(c,state)) return 6;
    frames(c,120,0);
    if(!c->loadState(c,state)) return 7;
    frames(c,60,0);
    uint64_t replay=hash();
    if(!c->loadState(c,state)) return 8;
    frames(c,60,0);
    if(replay!=hash()) {fprintf(stderr,"State replay framebuffer mismatch\n");return 9;}
    printf("Core boot/input activity and deterministic emulator state replay passed; not cartridge saving or story/evolution verification.\n");
    free(state);
    c->deinit(c);
    return 0;
}
