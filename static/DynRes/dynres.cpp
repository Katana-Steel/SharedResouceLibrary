/*
    2018 (c) Rene 'Katana Steel' Kjellerup, distributed under the terms of
    the GNU General Public Licenses version 3 or later for details see:
    http://www.gnu.org/licenses/gpl.html
*/
#include <dlfcn.h>
#include <cstring>
#include <cinttypes>

typedef const char* (*resString)(uint32_t);

unsigned int LoadString(void *h, int id, char* buff, int len)
{
    auto s = (resString)dlsym(h, "LoadString");
    const char *tmp =  s(id);
    uint32_t out = 0;
    if(tmp != nullptr) {
        std::strncpy(buff, tmp, len);
        out = std::strlen(buff);
    }
    return out;
}

uint32_t GetStringSize(void *h, int id)
{
    auto s = (resString)dlsym(h, "LoadString");
    const char *tmp =  s(id);
    return std::strlen(tmp);
}
