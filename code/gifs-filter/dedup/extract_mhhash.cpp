#include <stdint.h>
#include <iostream>
#include <bitset>
#include "pHash.h"
#include <fstream>
#include <vector>

using namespace std;

int main(int argc, char **argv) {

    const int alpha = 2;
    const int level = 1;

    vector<string> imgs;
    //vector<uint8_t *> hashes;
    vector<ulong64> hashes;
    string img_path;
    int hashlen = sizeof(ulong64);
    int pid = ::getpid();
    cerr << "started: " << pid << endl;
    while (cin >> img_path)
    {
        ulong64 hash = 0L;

        //hash = ph_mh_imagehash(img_path.c_str(), hashlen, alpha, level);
        //if (hash == NULL)
        int res = 0;
        try {
            res = ph_dct_imagehash(img_path.c_str(), hash);
        } catch (...)
        {}
        if(res)
        {
            std::cerr << "hash extract error" << std::endl;
            continue;
        }
        hashes.push_back(hash);
        imgs.push_back(img_path);
    }
    char *save_dir = argv[1];

    const int kBufferSize = 300;
    int i = 0;
    char save_path[kBufferSize];
    snprintf(save_path, kBufferSize, "%s/hash.%d", save_dir, pid);
    ofstream hash_out(save_path, ios::out | ios::binary);
    for (i = 0; i < hashes.size(); i++) {
        hash_out.write((const char*)&hashes[i], hashlen);
        //free(hashes[i]);
    }
    snprintf(save_path, kBufferSize, "%s/img.%d", save_dir, pid);
    ofstream img_out(save_path, ios::out);
    for (i = 0; i < hashes.size(); i++) {
        img_out << imgs[i] << endl;
    }
    return 0;
}
