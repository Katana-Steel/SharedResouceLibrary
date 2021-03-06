/*
  my template c++ file which implements the internal resource
  lookup and storage
*/
#include "dynres.h"
#include <string>
#include <cinttypes>
#include <utility>
#include <algorithm>
#include <vector>

${defines}

std::vector<std::pair<uint32_t,const char*>> str_tab {
${string_table}
    std::make_pair(0,"generated by LithTech Resource compiler\n\n" \
    "2018 (c) Rene 'Katana Steel' Kjellerup, distributed under the terms" \
    " of\nthe GNU General Public Licenses version 3 or later for details" \
    " see:\nhttp://www.gnu.org/licenses/gpl.html\n")
};
extern "C" {
  const char* LoadString(uint32_t id)
  {
    auto res = std::find_if(str_tab.begin(),
                            str_tab.end(),
                            [id](std::pair<uint32_t, const char*> x){
                                return (x.first == id);
                            });
    if(res != str_tab.end())
        return res->second;
    else
        return nullptr;
  }
}
void setup_cursors() { }
void setup_string_tables() {
    bool c = false;
    for(auto&& p : str_tab)
        c = (LoadString(p.first) == p.second);
}
